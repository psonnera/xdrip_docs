// Translation helpers shared by config, fallback routes and the build.
// Layout: English at docs/<path>.md, translations at docs/fr/<path>.md and docs/it/<path>.md.
import { createHash } from 'node:crypto'
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs'
import { dirname, join, posix, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

export const DOCS = resolve(dirname(fileURLToPath(import.meta.url)), '..')
export const LOCALES = ['fr', 'it'] as const
export type Locale = (typeof LOCALES)[number]
const NOT_PAGES = ['.vitepress', 'public', 'node_modules', ...LOCALES]

/** Hash of an English page, line-ending independent. Same algorithm as .claude/scripts/i18n-status.py */
export function sourceHash(file: string): string {
  const text = readFileSync(file).toString('binary').replace(/\r\n/g, '\n')
  return createHash('sha1').update(Buffer.from(text, 'binary')).digest('hex').slice(0, 10)
}

/** All English pages, docs-relative posix paths ("use/alarms.md"). */
export function englishPages(dir = ''): string[] {
  const out: string[] = []
  for (const name of readdirSync(join(DOCS, dir))) {
    const rel = dir ? `${dir}/${name}` : name
    if (!dir && NOT_PAGES.includes(name)) continue
    if (statSync(join(DOCS, rel)).isDirectory()) out.push(...englishPages(rel))
    else if (name.endsWith('.md') && !name.includes('[')) out.push(rel)
  }
  return out
}

export function localeOf(relativePath: string): Locale | undefined {
  return LOCALES.find((l) => relativePath.startsWith(`${l}/`))
}

/** English pages with no translation yet in `locale`, as [dir, page] (dir '' = docs root). */
export function untranslated(locale: Locale): [string, string][] {
  return englishPages()
    .filter((p) => !existsSync(join(DOCS, locale, p)))
    .map((p) => [posix.dirname(p) === '.' ? '' : posix.dirname(p), posix.basename(p, '.md')])
}

/** English page body for a fallback route (front matter dropped). */
export function englishBody(rel: string): string {
  return readFileSync(join(DOCS, rel), 'utf-8').replace(/\r\n/g, '\n').replace(/^---\n[\s\S]*?\n---\n/, '')
}

/**
 * Translated pages are written exactly like their English page: an image path such as
 * ../images/x.png points into the locale tree. Use the localized file if it exists
 * (docs/fr/use/images/x.png), otherwise point to the English one.
 */
export function localizeAsset(src: string, relativePath: string): string {
  const locale = localeOf(relativePath)
  if (!locale || /^([a-z][a-z0-9+.-]*:|\/|#)/i.test(src)) return src
  const [path, rest = ''] = src.split(/(?=[?#])/)
  const pageDir = posix.dirname(relativePath)
  const target = posix.normalize(posix.join(pageDir, path))
  if (existsSync(join(DOCS, target))) return src
  const english = target.slice(locale.length + 1)
  if (!existsSync(join(DOCS, english))) return src
  let out = posix.relative(pageDir, english)
  if (!out.startsWith('.')) out = `./${out}`
  return out + rest
}

export const NOTICE_SKIP = ['changelog.md']
