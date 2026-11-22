import { defineConfig, type DefaultTheme } from 'vitepress'
import container from 'markdown-it-container'
import { existsSync } from 'node:fs'
import { join } from 'node:path'
import { sections, type Label } from './sidebar.mts'
import { DOCS, LOCALES, localeOf, localizeAsset, sourceHash, NOTICE_SKIP } from './i18n.mts'

type Lang = keyof Label

function sidebar(lang: Lang): DefaultTheme.SidebarItem[] {
  const prefix = lang === 'en' ? '' : `/${lang}`
  return sections.map((s) =>
    s.items
      ? {
          text: s.text[lang],
          collapsed: true,
          items: s.items.map((i) => ({ text: i.text[lang], link: prefix + i.link })),
        }
      : { text: s.text[lang], link: prefix + s.link },
  )
}

// Page title for the browser tab: pages have no H1, use the sidebar label.
const labels = new Map<string, Label>()
for (const s of sections) for (const i of s.items ?? [s as any]) labels.set(i.link.slice(1) + '.md', i.text)

// Anchors identical to the MkDocs ones (Python-Markdown toc slugify), so existing #links keep working.
const slugify = (s: string) =>
  s
    .normalize('NFKD')
    .replace(/[^\x00-\x7F]/g, '')
    .replace(/[^\w\s-]/g, '')
    .trim()
    .toLowerCase()
    .replace(/[-\s]+/g, '-')

/** xDrip menu mock-ups: ::: xdrip <title> / ::: xdripitem <title> */
function xdripBoxes(md: any) {
  for (const name of ['xdrip', 'xdripitem']) {
    md.use(container, name, {
      validate: (params: string) => params.trim().split(/\s+/)[0] === name,
      render(tokens: any[], idx: number, _o: any, env: any) {
        const t = tokens[idx]
        if (t.nesting !== 1) return '</div>\n'
        const title = t.info.trim().slice(name.length).trim()
        const head = title ? `<p class="admonition-title">${md.renderInline(title, env)}</p>\n` : ''
        return `<div class="admonition ${name}">\n${head}`
      },
    })
  }
}

/** Translated pages reuse the English images unless a localized copy exists. */
function localizedAssets(md: any) {
  const attr = /(\b(?:src|href)=)(["'])([^"']*)\2/g
  const fixHtml = (html: string, rp: string) => html.replace(attr, (_m, a, q, v) => a + q + localizeAsset(v, rp) + q)
  const walk = (tokens: any[], rp: string) => {
    for (const t of tokens) {
      if (t.type === 'image') t.attrSet('src', localizeAsset(t.attrGet('src'), rp))
      else if (t.type === 'html_inline' || t.type === 'html_block') t.content = fixHtml(t.content, rp)
      else if (t.type === 'link_open' && /\.(png|jpe?g|gif|svg|webp|pdf|html)([?#]|$)/i.test(t.attrGet('href') ?? ''))
        t.attrSet('href', localizeAsset(t.attrGet('href'), rp))
      else if (t.type === 'container_xdrip_open' || t.type === 'container_xdripitem_open') t.info = fixHtml(t.info, rp)
      if (t.children) walk(t.children, rp)
    }
  }
  md.core.ruler.push('xdrip_localized_assets', (state: any) => {
    const rp = state.env?.relativePath
    if (rp && localeOf(rp)) walk(state.tokens, rp)
  })
}

const ui = {
  fr: {
    outline: { label: 'Sur cette page' },
    docFooter: { prev: 'Page précédente', next: 'Page suivante' },
    darkModeSwitchLabel: 'Apparence',
    lightModeSwitchTitle: 'Passer au thème clair',
    darkModeSwitchTitle: 'Passer au thème sombre',
    sidebarMenuLabel: 'Menu',
    returnToTopLabel: 'Retour en haut',
    langMenuLabel: 'Changer de langue',
    notFound: { title: 'PAGE INTROUVABLE', quote: "Cette page n'existe pas.", linkText: "Retour à l'accueil" },
  },
  it: {
    outline: { label: 'In questa pagina' },
    docFooter: { prev: 'Pagina precedente', next: 'Pagina successiva' },
    darkModeSwitchLabel: 'Aspetto',
    lightModeSwitchTitle: 'Passa al tema chiaro',
    darkModeSwitchTitle: 'Passa al tema scuro',
    sidebarMenuLabel: 'Menu',
    returnToTopLabel: 'Torna su',
    langMenuLabel: 'Cambia lingua',
    notFound: { title: 'PAGINA NON TROVATA', quote: 'Questa pagina non esiste.', linkText: 'Torna alla home' },
  },
}

const search = {
  fr: {
    translations: {
      button: { buttonText: 'Rechercher', buttonAriaLabel: 'Rechercher' },
      modal: {
        displayDetails: 'Afficher la liste détaillée',
        resetButtonTitle: 'Effacer la recherche',
        backButtonTitle: 'Fermer la recherche',
        noResultsText: 'Aucun résultat pour',
        footer: { selectText: 'sélectionner', navigateText: 'naviguer', closeText: 'fermer' },
      },
    },
  },
  it: {
    translations: {
      button: { buttonText: 'Cerca', buttonAriaLabel: 'Cerca' },
      modal: {
        displayDetails: 'Mostra elenco dettagliato',
        resetButtonTitle: 'Cancella ricerca',
        backButtonTitle: 'Chiudi ricerca',
        noResultsText: 'Nessun risultato per',
        footer: { selectText: 'seleziona', navigateText: 'naviga', closeText: 'chiudi' },
      },
    },
  },
}

export default defineConfig({
  title: 'xDrip',
  description: 'xDrip documentation',
  base: '/xdrip_docs/',
  cleanUrls: false,
  // Standalone tool page (not Markdown), copied as is by legacy-redirects.mjs
  ignoreDeadLinks: [/nocturne-qr/],
  head: [['link', { rel: 'icon', href: '/xdrip_docs/xDriplogo.png' }]],

  locales: {
    root: { label: 'English', lang: 'en', themeConfig: { sidebar: sidebar('en') } },
    fr: { label: 'Français', lang: 'fr', themeConfig: { sidebar: sidebar('fr'), ...ui.fr } },
    it: { label: 'Italiano', lang: 'it', themeConfig: { sidebar: sidebar('it'), ...ui.it } },
  },

  themeConfig: {
    logo: '/xDriplogo.png',
    outline: { level: [2, 3] },
    socialLinks: [{ icon: 'github', link: 'https://github.com/xdrip/xdrip_docs' }],
    search: { provider: 'local', options: { locales: search } },
  },

  markdown: {
    anchor: { slugify },
    container: { infoLabel: 'Info', warningLabel: 'Warning', tipLabel: 'Tip', dangerLabel: 'Danger' },
    config(md) {
      md.use(xdripBoxes)
      md.use(localizedAssets)
    },
  },

  transformPageData(pageData) {
    const rp = pageData.relativePath
    const locale = localeOf(rp)
    const english = locale ? rp.slice(locale.length + 1) : rp
    const label = labels.get(english)
    if (label && !pageData.frontmatter.title) pageData.title = label[(locale ?? 'en') as Lang]
    if (!locale || pageData.frontmatter.i18n_fallback || NOTICE_SKIP.includes(english)) return
    const src = join(DOCS, english)
    if (existsSync(src) && String(pageData.frontmatter.source_hash) !== sourceHash(src))
      pageData.frontmatter.i18n_outdated = true
  },
})

