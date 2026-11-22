#!/usr/bin/env python3
"""Translation status of the docs, per language.

  python .claude/scripts/i18n-status.py              # summary: translated / outdated / missing
  python .claude/scripts/i18n-status.py --list       # also list every outdated and missing page
  python .claude/scripts/i18n-status.py --diff fr    # English changes since each fr page was translated
  python .claude/scripts/i18n-status.py --stamp docs/use/alarms.fr.md [...]
                                                     # record the current English hash in the
                                                     # translation's front matter (after updating it)

A translation's front matter carries `source_hash` (hash of the English page it matches) and
`source_commit` (commit of the English page at that time, used by --diff).
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
sys.path.insert(0, str(ROOT / "hooks"))
from i18n_notices import source_hash, english_source  # noqa: E402

LOCALES = ["fr", "it"]
FM = re.compile(r"\A---\n(?:(.*?)\n)?---\n", re.S)


def english_pages():
    return sorted(p for p in DOCS.rglob("*.md")
                  if not any(p.name.endswith(f".{l}.md") for l in LOCALES))


def read_meta(path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = FM.match(text)
    meta = {}
    if m:
        for line in (m.group(1) or "").splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip("'\"")
    return meta, text, m


def last_commit(path):
    r = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%h", "--", str(path)],
                       capture_output=True, text=True)
    return r.stdout.strip()


def stamp(path):
    path = Path(path).resolve()
    locale = path.name.split(".")[-2]
    src = english_source(path, locale)
    meta, text, m = read_meta(path)
    meta["source_hash"] = source_hash(src)
    meta["source_commit"] = last_commit(src)
    body = text[m.end():] if m else text
    fm = "\n".join(f"{k}: {v}" for k, v in meta.items())
    path.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8", newline="\n")
    print(f"stamped {path.relative_to(ROOT)} -> {meta['source_hash']} ({meta['source_commit']})")


def status():
    out = {}
    for locale in LOCALES:
        done, outdated, missing = [], [], []
        for en in english_pages():
            tr = en.with_name(en.name[:-3] + f".{locale}.md")
            if not tr.exists():
                missing.append(en)
            elif read_meta(tr)[0].get("source_hash") != source_hash(en):
                outdated.append(tr)
            else:
                done.append(tr)
        out[locale] = (done, outdated, missing)
    return out


def main(argv):
    if argv[:1] == ["--stamp"]:
        for p in argv[1:]:
            stamp(p)
        return
    st = status()
    if argv[:1] == ["--diff"]:
        locale = argv[1]
        for tr in st[locale][1]:
            meta = read_meta(tr)[0]
            src = english_source(tr, locale)
            print(f"\n===== {tr.relative_to(ROOT)} (translated from {meta.get('source_commit', '?')})")
            base = meta.get("source_commit")
            cmd = ["git", "-C", str(ROOT), "diff", base, "--", str(src)] if base else \
                  ["git", "-C", str(ROOT), "log", "-3", "-p", "--", str(src)]
            print(subprocess.run(cmd, capture_output=True, text=True).stdout)
        return
    total = len(english_pages())
    for locale, (done, outdated, missing) in st.items():
        print(f"{locale}: {len(done)}/{total} up to date, {len(outdated)} outdated, {len(missing)} missing")
        if argv[:1] == ["--list"]:
            for p in outdated:
                print(f"   outdated  {p.relative_to(DOCS)}")
            for p in missing:
                print(f"   missing   {p.relative_to(DOCS)}")


if __name__ == "__main__":
    main(sys.argv[1:])
