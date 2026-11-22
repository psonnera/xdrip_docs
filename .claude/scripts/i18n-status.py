#!/usr/bin/env python3
"""Translation status of the docs, per language.

  python .claude/scripts/i18n-status.py              # summary: up to date / outdated / missing
  python .claude/scripts/i18n-status.py --list       # also list every outdated and missing page
  python .claude/scripts/i18n-status.py --diff fr    # English changes since each outdated fr page was translated
  python .claude/scripts/i18n-status.py --start fr use/alarms.md
                                                     # create docs/fr/use/alarms.md from the English page
  python .claude/scripts/i18n-status.py --anchors docs/fr/use/alarms.md [...]
                                                     # give every translated heading its English anchor
                                                     # ({#id}), so #links work from every language
                                                     # (reads the built site: run `npm run docs:build` first)
  python .claude/scripts/i18n-status.py --stamp docs/fr/use/alarms.md [...]
                                                     # record the current English hash in the translation's
                                                     # front matter (after translating / updating it)

Layout: English docs/<path>.md, translations docs/fr/<path>.md and docs/it/<path>.md.
A translation's front matter carries `source_hash` (hash of the English page it matches) and
`source_commit` (last commit of the English page at that time, used by --diff).
The hash must stay identical to sourceHash() in docs/.vitepress/i18n.mts (the site shows the
"outdated" notice from it).
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
DIST = DOCS / ".vitepress" / "dist"
LOCALES = ["fr", "it"]
SKIP = {".vitepress", "public", "node_modules", *LOCALES}
FM = re.compile(r"\A---\n(?:(.*?)\n)?---\n", re.S)
HEAD = re.compile(r"^(#{1,6}\s.*?)(?:\s*\{#[^}]*\})?\s*$")


def source_hash(path: Path) -> str:
    return hashlib.sha1(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:10]


def english_pages():
    return sorted(p for p in DOCS.rglob("*.md")
                  if p.relative_to(DOCS).parts[0] not in SKIP and "[" not in p.name)


def split(path: Path):
    """translation path -> (locale, English path)"""
    rel = path.resolve().relative_to(DOCS)
    return rel.parts[0], DOCS.joinpath(*rel.parts[1:])


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


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).stdout


def stamp(path):
    path = Path(path).resolve()
    _, src = split(path)
    meta, text, m = read_meta(path)
    meta["source_hash"] = source_hash(src)
    meta["source_commit"] = git("log", "-1", "--format=%h", "--", str(src)).strip()
    body = text[m.end():] if m else text
    fm = "\n".join(f"{k}: {v}" for k, v in meta.items())
    path.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8", newline="\n")
    print(f"stamped {path.relative_to(ROOT).as_posix()} -> {meta['source_hash']} ({meta['source_commit']})")


def headings(lines):
    """indexes of the ATX heading lines outside code fences"""
    out, fence = [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and re.match(r"#{1,6}\s", line):
            out.append(i)
    return out


def anchors(path):
    """Copy the English heading ids onto the translation, heading by heading (same structure)."""
    path = Path(path).resolve()
    _, src = split(path)
    html = DIST / src.relative_to(DOCS).with_suffix(".html")
    if not html.exists() or html.stat().st_mtime < src.stat().st_mtime:
        sys.exit(f"{html.relative_to(ROOT).as_posix()} missing or older than the English page: run npm run docs:build")
    body = re.search(r'class="vp-doc[\s\S]*?(?=<footer class="VPDocFooter")',
                     html.read_text(encoding="utf-8")).group(0)
    ids = re.findall(r'<h[1-6][^>]*\bid="([^"]*)"', body)
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    idx = headings(lines)
    if len(idx) != len(ids):
        sys.exit(f"{path.relative_to(ROOT).as_posix()}: {len(idx)} headings, English has {len(ids)}: "
                 "make the structure identical first")
    for i, a in zip(idx, ids):
        lines[i] = HEAD.match(lines[i]).group(1).rstrip() + f" {{#{a}}}"
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"anchors {path.relative_to(ROOT).as_posix()}: {len(ids)} headings")


def start(locale, rel):
    src, dest = DOCS / rel, DOCS / locale / rel
    if dest.exists():
        sys.exit(f"{dest.relative_to(ROOT)} already exists")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(src.read_text(encoding="utf-8").replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    print(f"created {dest.relative_to(ROOT).as_posix()} (English copy): translate it, then --anchors and --stamp it")


def status():
    out = {}
    for locale in LOCALES:
        done, outdated, missing = [], [], []
        for en in english_pages():
            tr = DOCS / locale / en.relative_to(DOCS)
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
    if argv[:1] == ["--anchors"]:
        for p in argv[1:]:
            anchors(p)
        return
    if argv[:1] == ["--start"]:
        start(argv[1], argv[2])
        return
    st = status()
    if argv[:1] == ["--diff"]:
        locale = argv[1]
        for tr in st[locale][1]:
            meta = read_meta(tr)[0]
            _, src = split(tr)
            base = meta.get("source_commit")
            print(f"\n===== {tr.relative_to(ROOT).as_posix()} (translated from {base or '?'})")
            print(git("diff", base, "--", str(src)) if base else git("log", "-3", "-p", "--", str(src)))
        return
    total = len(english_pages())
    for locale, (done, outdated, missing) in st.items():
        print(f"{locale}: {len(done)}/{total} up to date, {len(outdated)} outdated, {len(missing)} missing")
        if argv[:1] == ["--list"]:
            for p in outdated:
                print(f"   outdated  {p.relative_to(DOCS / locale).as_posix()}")
            for p in missing:
                print(f"   missing   {p.relative_to(DOCS).as_posix()}")


if __name__ == "__main__":
    main(sys.argv[1:])
