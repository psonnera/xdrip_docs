# Translations

The site is built with [VitePress](https://vitepress.dev/) in English, French and Italian from one repository:

```
docs/use/alarms.md            English, the reference version
docs/fr/use/alarms.md         French
docs/it/use/alarms.md         Italian
docs/use/images/x.png         used by all languages
docs/fr/use/images/x.png      optional French screenshot, used instead of the English one
```

- Published at https://psonnera.github.io/xdrip_docs/ (English), `/fr/` and `/it/`.
- A page with no translation is still served under `/fr/` and `/it/`: the English text with a "not translated yet"
  notice (fallback routes `docs/<locale>/[page].md` and `docs/<locale>/[dir]/[page].md`, nothing to maintain).
- A translation whose English page changed after it was translated shows an "outdated" notice with a link to the English page.
- Sidebar labels for all languages: `docs/.vitepress/sidebar.mts`. When a page is added, add it there with its three labels.
- `changelog.md` stays English only (no notice).

Run locally: `npm install` once, then `npm run docs:dev` (live preview) or `npm run docs:build` (full check: dead links
and invalid HTML fail the build).

## Workflow

1. **Start** a translation from the English page: `python .claude/scripts/i18n-status.py --start fr use/alarms.md`
   (copies it to `docs/fr/use/alarms.md`). Translate the text in place: keep links and image paths exactly as in the
   English page, they resolve to the right language and to the English images automatically.
2. **Anchors and stamp** when done: `npm run docs:build`, then
   `python .claude/scripts/i18n-status.py --anchors docs/fr/use/alarms.md` (English heading ids) and
   `python .claude/scripts/i18n-status.py --stamp docs/fr/use/alarms.md` (records which English version it matches)
   (commit the English page first if you also edited it, so `source_commit` is right.)
3. **Check status** any time: `python .claude/scripts/i18n-status.py --list`.
   `--diff fr` prints the English diff of every outdated French page since it was translated: apply it, then stamp.
4. **After a release**: `/release-update` ends by updating the translations of the English pages it edited (step 5b).

## UI terminology: `ui-strings.tsv`

When a page names a menu, setting, button or screen, use **the exact text xDrip shows in that language**,
even when the app's translation is clumsy: the reader has to find it on their phone.
`ui-strings.tsv` holds every app string in en / fr / it, extracted from a release tag. Refresh it after a release:

```
python .claude/scripts/ui-strings.py "C:/Data/50 - My Projects/xDrip+/xDrip" <tag>
```

Search it for the English label (`grep -i "Less common settings" i18n/ui-strings.tsv`). If the fr/it column is empty
the app shows English: keep the English label. Some preference screens are not translated in the app at all; keep the
English label then too, optionally followed by a translation in parentheses on its first occurrence.

## Page syntax

- xDrip menu mock-ups: `::: xdrip <title>` and `::: xdripitem <title>` … `:::` (the title may contain HTML, e.g. the
  ON/OFF `<span class='symbol'><img …></span>`). Notes: `::: info <title>`, `::: warning <title>`, `::: tip`.
  Leave a blank line before a box. A box inside a box uses a longer fence on the outer one (`::::`).
- Raw HTML must be valid (every `<span>` closed, `<br>` not `</br>`); write `&lt;` for a literal `<` in text.
- Box titles in translations are written out (`::: warning Attention`), the default labels are English.

## Common rules

- Translate meaning, not word by word; keep the page structure (headings, lists, boxes, images) identical so the two versions can be compared.
- Keep unchanged: links, image paths, HTML, code, file names, version numbers.
- **Headings**: a translated heading keeps its English anchor (`## Écran principal {#main-view}`), added by
  `i18n-status.py --anchors` once the page is translated. Links keep the English anchors (`./g7#pairing`) and work
  whether or not the target page is translated. This needs the same headings, in the same order, as the English page.
- Never translate product and brand names: xDrip, Nightscout, AndroidAPS, Dexcom G6/G7, ONE, ONE+, Stelo, Libre, Libre 2, Li3, Eversense, CareLink, Tidepool, Nocturne, BYODA, Juggluco, WatchDrip, BlueJay, MiBand, Wear OS…
  Keep full Abbott names (FreeStyle Libre): this site does not obfuscate them.
- Keep technical names users will meet elsewhere in English, with the term the app uses: Bluetooth, NFC, OOP, ADB, Nightly, Engineering mode (but translate the sentence around it).
- Units: mg/dL and mmol/L unchanged. Decimal separator follows the language (5,5 mmol/L) in prose, never inside screenshots or code.

## French (`docs/fr/`)

- **Vouvoiement** ("vous") everywhere, imperative in the "vous" form ("Appuyez sur…", "Sélectionnez…").
- Plain space before `:` `?` `!`.
- See `glossary.fr.md`.

## Italian (`docs/it/`)

- **Tu** everywhere, imperative in the "tu" form ("Tocca…", "Seleziona…").
- See `glossary.it.md`.
