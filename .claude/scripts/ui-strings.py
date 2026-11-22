#!/usr/bin/env python3
"""Extract xDrip UI strings (en / fr / it) from a release tag into i18n/ui-strings.tsv.

The table is the terminology reference for translating the docs: whenever a page names a
setting, menu or button, use the fr/it text the app itself shows.

Usage:  python .claude/scripts/ui-strings.py <xdrip_repo_path> <tag>
Reads via `git show <tag>:...` so the clone's checked-out branch does not matter.
"""
import csv
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

RES = "app/src/main/res"
SOURCES = {
    "en": ["values/strings.xml", "values/strings_activity_preferences.xml"],
    "fr": ["values-fr/strings-fr.xml"],
    "it": ["values-it/strings-it.xml"],
}


def git_show(repo, tag, path):
    r = subprocess.run(["git", "-C", repo, "show", f"{tag}:{RES}/{path}"],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def text_of(el):
    s = "".join(el.itertext()).strip()
    if len(s) >= 2 and s[0] == s[-1] == '"':
        s = s[1:-1]
    return s.replace("\\'", "'").replace('\\"', '"').replace("\\n", " ").replace("\t", " ")


def load(repo, tag, files):
    out = {}
    for f in files:
        data = git_show(repo, tag, f)
        if data is None:
            continue
        for el in ET.fromstring(data).iter("string"):
            name = el.get("name")
            if name and el.get("translatable") != "false":
                out[name] = text_of(el)
    return out


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    repo, tag = sys.argv[1], sys.argv[2]
    tables = {lang: load(repo, tag, files) for lang, files in SOURCES.items()}
    dest = Path(__file__).resolve().parents[2] / "i18n" / "ui-strings.tsv"
    dest.parent.mkdir(exist_ok=True)
    with dest.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow([f"# xDrip {tag}", "en", "fr", "it"])
        for name in sorted(tables["en"]):
            w.writerow([name, tables["en"][name],
                        tables["fr"].get(name, ""), tables["it"].get(name, "")])
    print(f"{dest}: {len(tables['en'])} strings "
          f"(fr {sum(1 for n in tables['en'] if n in tables['fr'])}, "
          f"it {sum(1 for n in tables['en'] if n in tables['it'])})")


if __name__ == "__main__":
    main()
