# Translations

The site is built in English, French and Italian from one source tree with
[mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/) (suffix structure):

```
docs/use/alarms.md        English, the reference version
docs/use/alarms.fr.md     French
docs/use/alarms.it.md     Italian
docs/use/images/x.png     shared by all languages
docs/use/images/x.fr.png  optional localized screenshot, picked up automatically
```

- Published at https://psonnera.github.io/xdrip_docs/ (English), `/fr/` and `/it/`.
- A page with no translation is served in English under `/fr/` or `/it/`, with a "not translated yet" notice.
- A translation whose English page changed after it was translated gets an "outdated" notice (see `hooks/i18n_notices.py`).
- Nav labels are translated in `mkdocs.yml` (`nav_translations`). When a page is added to `nav`, add its label to both languages.
- `changelog.md` stays English only.

## Workflow

1. **Translate or update** `page.fr.md` / `page.it.md`, following the rules below.
2. **Stamp it** so it is recorded as matching the current English page:
   `python .claude/scripts/i18n-status.py --stamp docs/use/alarms.fr.md docs/use/alarms.it.md`
   (commit the English change first if you also edited it, so `source_commit` is right.)
3. **Check status** any time: `python .claude/scripts/i18n-status.py --list`.
   `--diff fr` prints the English diff of every outdated French page since it was translated: apply that diff to the translation, then stamp.
4. **After a release**: `/release-update` ends by updating the translations of the English pages it edited.

Test locally: `pip install -r docs/requirements.txt`, then `mkdocs serve`.

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

## Common rules

- Translate meaning, not word by word; keep the page structure (headings, lists, admonitions, images) identical so the two versions can be compared.
- Keep unchanged: links, anchors (`#language`), image paths, HTML, code, file names, version numbers.
- Admonition types stay English (`!!!info`, `!!!warning`), their titles and bodies are translated.
- Never translate product and brand names: xDrip, Nightscout, AndroidAPS, Dexcom G6/G7, ONE, ONE+, Stelo, Libre, Libre 2, Li3, Eversense, CareLink, Tidepool, Nocturne, BYODA, Juggluco, WatchDrip, BlueJay, MiBand, Wear OS…
  Keep full Abbott names (FreeStyle Libre): this site does not obfuscate them.
- Keep technical names users will meet elsewhere in English, with the term the app uses: Bluetooth, NFC, OOP, ADB, Nightly, Engineering mode (but translate the sentence around it).
- Units: mg/dL and mmol/L unchanged. Decimal separator follows the language (5,5 mmol/L) in prose, never inside screenshots or code.

## French (`.fr.md`)

- **Vouvoiement** ("vous") everywhere, imperative in the "vous" form ("Appuyez sur…", "Sélectionnez…").
- Typography: non-breaking space before `: ; ! ?` and inside « guillemets » is optional in Markdown; use a plain space before `:` `?` `!`.
- See `glossary.fr.md`.

## Italian (`.it.md`)

- **Tu** everywhere, imperative in the "tu" form ("Tocca…", "Seleziona…").
- See `glossary.it.md`.
