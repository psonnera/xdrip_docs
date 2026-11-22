// Post-build step (npm run docs:build):
// 1. The MkDocs site used folder URLs (/xdrip_docs/use/alarms/). VitePress pages are
//    /xdrip_docs/use/alarms.html: write a redirect at each old URL, keeping #anchors,
//    so links in forums, other docs and bookmarks keep working.
// 2. Copy the images as plain files too: raw <a href="images/x.png"> links (click to enlarge)
//    are not bundled by Vite.
import { copyFileSync, existsSync, mkdirSync, readdirSync, statSync, writeFileSync } from 'node:fs'
import { dirname, join, relative, sep } from 'node:path'
import { fileURLToPath } from 'node:url'

const DOCS = join(dirname(fileURLToPath(import.meta.url)), '..')
const DIST = join(DOCS, '.vitepress', 'dist')
const SKIP = new Set(['.vitepress', 'public', 'fr', 'it'])

function walk(dir, skipTop, out = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name)
    if (skipTop && dir === skipTop.root && skipTop.names.has(name)) continue
    statSync(p).isDirectory() ? walk(p, skipTop, out) : out.push(p)
  }
  return out
}

let redirects = 0
for (const file of walk(DIST, { root: DIST, names: new Set(['assets', 'fr', 'it']) })) {
  const rel = relative(DIST, file).split(sep).join('/')
  if (!rel.endsWith('.html') || rel.endsWith('index.html') || rel === '404.html') continue
  const page = rel.slice(0, -5)
  const target = `../${page.split('/').pop()}.html`
  const stub = join(DIST, page, 'index.html')
  if (existsSync(stub)) continue
  mkdirSync(dirname(stub), { recursive: true })
  writeFileSync(stub, `<!doctype html><html><head><meta charset="utf-8"><title>xDrip</title>
<link rel="canonical" href="${target}"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=${target}">
<script>location.replace(${JSON.stringify(target)} + location.search + location.hash)</script>
</head><body><a href="${target}">${page}</a></body></html>\n`)
  redirects++
}

let copied = 0
for (const file of walk(DOCS, { root: DOCS, names: SKIP })) {
  if (/\.(md|mts|ts|vue|css|mjs|txt)$/.test(file)) continue
  const dest = join(DIST, relative(DOCS, file))
  if (existsSync(dest)) continue
  mkdirSync(dirname(dest), { recursive: true })
  copyFileSync(file, dest)
  copied++
}
console.log(`legacy-redirects: ${redirects} redirects, ${copied} images copied`)
