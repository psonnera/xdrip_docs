"""MkDocs hook: add a notice on pages that are not (or no longer) up to date in the reader's language.

- Fallback page (English content served under /fr/ or /it/): "not translated yet" notice.
- Translated page whose `source_hash` front matter no longer matches its English page:
  "the English version has changed since" notice, linking to it.

`source_hash` is written by `.claude/scripts/i18n-status.py --stamp`; both use source_hash() below.
"""
import hashlib
import posixpath
import re
from pathlib import Path

DEFAULT = "en"

NOTICES = {
    "fr": {
        "missing": ('!!! info "Page pas encore traduite"\n'
                    "    Cette page n'est pas encore disponible en français : "
                    "vous lisez la version anglaise.\n\n"),
        "outdated": ('!!! warning "Traduction à mettre à jour"\n'
                     "    La version anglaise de cette page a été modifiée depuis sa traduction. "
                     "Consultez [la version anglaise]({url}) pour les dernières informations.\n\n"),
    },
    "it": {
        "missing": ('!!! info "Pagina non ancora tradotta"\n'
                    "    Questa pagina non è ancora disponibile in italiano: "
                    "stai leggendo la versione inglese.\n\n"),
        "outdated": ('!!! warning "Traduzione da aggiornare"\n'
                     "    La versione inglese di questa pagina è stata modificata dopo la traduzione. "
                     "Consulta [la versione inglese]({url}) per le informazioni più recenti.\n\n"),
    },
}


def source_hash(path: Path) -> str:
    """Hash of the English page, line-ending independent (Windows checkout vs CI)."""
    text = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(text).hexdigest()[:10]


def english_source(path: Path, locale: str) -> Path:
    # use/alarms.fr.md -> use/alarms.md
    return path.with_name(path.name.replace(f".{locale}.md", ".md"))


def english_url(page, locale: str, config) -> str:
    # page.url is "fr/use/alarms/"; site root relative link back to the English page
    url = page.url[len(locale) + 1:] if page.url.startswith(locale + "/") else page.url
    depth = page.url.count("/")
    return "../" * depth + url


RAW_SRC = re.compile(r'(\bsrc=["\'])(?![a-z][a-z0-9+.-]*:|/|#|data:)([^"\']+)', re.I)


def fix_raw_html_assets(markdown, page, locale, docs_dir):
    """Raw HTML <img src="../../images/x.png"> is not rewritten by MkDocs, and under /fr/ the page
    sits one folder deeper while shared images stay in the English tree: point back to them.
    If a localized image exists (x.fr.png), the i18n plugin publishes it at /fr/.../x.png: keep the path."""
    en_url = page.url[len(locale) + 1:]          # "use/3dotsmenu/"
    to_root = "../" * page.url.count("/")        # from /fr/use/3dotsmenu/ to the site root
    def repl(m):
        target = posixpath.normpath(posixpath.join(en_url, m.group(2)))   # "use/images/x.png"
        stem, ext = posixpath.splitext(target)
        if (Path(docs_dir) / f"{stem}.{locale}{ext}").exists():
            return m.group(0)
        return m.group(1) + to_root + target
    return RAW_SRC.sub(repl, markdown)


def on_page_markdown(markdown, page, config, files):
    build_locale = getattr(page.file, "locale_alternate_of", DEFAULT)
    file_locale = getattr(page.file, "locale", DEFAULT)
    notices = NOTICES.get(build_locale)
    if notices is None:
        return markdown

    markdown = fix_raw_html_assets(markdown, page, build_locale, config["docs_dir"])

    if file_locale != build_locale:
        if page.is_homepage or page.file.src_uri == "changelog.md":
            return markdown
        return notices["missing"] + markdown

    expected = page.meta.get("source_hash")
    src = english_source(Path(page.file.abs_src_path), build_locale)
    if src.exists() and str(expected) != source_hash(src):
        return notices["outdated"].format(url=english_url(page, build_locale, config)) + markdown
    return markdown
