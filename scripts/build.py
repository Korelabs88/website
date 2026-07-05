#!/usr/bin/env python3
"""Genera el sitio estático multilingüe de Korelabs en public/."""

from __future__ import annotations

import json
import re
import shutil
from datetime import date
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
CONTENT = ROOT / "content"
DIST = ROOT / "public"
SITE_URL = "https://alexkore.com"
LANGS = ("es", "en", "pt")
DEFAULT_LANG = "es"
TODAY = date.today().isoformat()

BLOG_PATH = "blog"
FAQ_PATH = {"es": "preguntas-frecuentes", "en": "faq", "pt": "perguntas-frequentes"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def page_key(page_type: str, slug: str | None = None) -> str:
    if page_type in ("home", "blog", "faq"):
        return page_type
    return f"{page_type}:{slug}"


def url_for(lang: str, page_type: str, slug: str | None = None) -> str:
    base = f"/{lang}/"
    if page_type == "home":
        return base
    if page_type == "product":
        return f"{base}{slug}/"
    if page_type == "faq":
        return f"{base}{FAQ_PATH[lang]}/"
    if page_type == "blog":
        return f"{base}{BLOG_PATH}/"
    if page_type == "article":
        return f"{base}{BLOG_PATH}/{slug}/"
    raise ValueError(f"Unknown page type: {page_type}")


def build_alternates(page_type: str, slug: str | None, registry: dict) -> dict[str, str]:
    alts: dict[str, str] = {}
    for lang in LANGS:
        if page_key(page_type, slug) in registry.get(lang, {}):
            alts[lang] = registry[lang][page_key(page_type, slug)]
    return alts


def parse_guide_md(text: str) -> tuple[dict, str]:
    meta: dict = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            body = parts[2].lstrip("\n")
    html = markdown.markdown(
        body,
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"permalink": False}},
    )
    return meta, html


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    return s[:64] or "section"


def extract_toc(html: str) -> tuple[str, list[dict]]:
    headings: list[dict] = []

    def repl(m: re.Match) -> str:
        level, hid, title = m.group(1), m.group(2), m.group(3)
        if not hid:
            hid = slugify(title)
        headings.append({"level": int(level), "id": hid, "title": title})
        return f'<h{level} id="{hid}">{title}</h{level}>'

    html = re.sub(r"<h([23])(?: id=\"([^\"]+)\")?>([^<]+)</h\1>", repl, html)
    return html, headings


def write_page(rel_path: str, html: str) -> None:
    out = DIST / rel_path.strip("/")
    if rel_path.endswith("/"):
        out = out / "index.html"
    else:
        out = out.with_suffix(".html") if not rel_path.endswith(".html") else out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def copy_static() -> None:
    for name in ("assets", "favicon.png", "_headers"):
        src = ROOT / name
        if src.is_dir():
            if (DIST / name).exists():
                shutil.rmtree(DIST / name)
            shutil.copytree(src, DIST / name)
        elif src.is_file():
            shutil.copy2(src, DIST / name)


def write_redirects() -> None:
    lines = [
        "/ /es/ 302",
        "/index.html /es/ 302",
        # URLs antiguas de guías → blog
        "/es/guias/* /es/blog/:splat 301",
        "/en/guides/* /en/blog/:splat 301",
        "/pt/guias/* /pt/blog/:splat 301",
    ]
    (DIST / "_redirects").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_robots() -> None:
    text = """User-agent: *
Allow: /

Sitemap: https://alexkore.com/sitemap.xml
"""
    (DIST / "robots.txt").write_text(text, encoding="utf-8")


def write_sitemaps(urls_by_lang: dict[str, list[str]]) -> None:
    def urlset(urls: list[str]) -> str:
        items = []
        for u in urls:
            items.append(
                f"  <url>\n    <loc>{SITE_URL}{u}</loc>\n"
                f"    <lastmod>{TODAY}</lastmod>\n"
                f"    <changefreq>weekly</changefreq>\n  </url>"
            )
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(items)
            + "\n</urlset>\n"
        )

    index_parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for lang in LANGS:
        fname = f"sitemap-{lang}.xml"
        (DIST / fname).write_text(urlset(urls_by_lang[lang]), encoding="utf-8")
        index_parts.append(f"  <sitemap>\n    <loc>{SITE_URL}/{fname}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </sitemap>")
    index_parts.append("</sitemapindex>")
    (DIST / "sitemap.xml").write_text("\n".join(index_parts) + "\n", encoding="utf-8")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.filters["url_for"] = lambda lang, pt, slug=None: url_for(lang, pt, slug)

    i18n = {lang: load_json(CONTENT / "i18n" / f"{lang}.json") for lang in LANGS}
    products_data = load_json(CONTENT / "products.json")
    faq_data = load_json(CONTENT / "faq.json")
    guides_manifest = load_json(CONTENT / "guides" / "manifest.json")

    registry: dict[str, dict[str, str]] = {lang: {} for lang in LANGS}
    urls_by_lang: dict[str, list[str]] = {lang: [] for lang in LANGS}

    def register(lang: str, ptype: str, slug: str | None, rel: str) -> None:
        registry[lang][page_key(ptype, slug)] = rel
        urls_by_lang[lang].append(rel)

    # --- Home ---
    for lang in LANGS:
        register(lang, "home", None, url_for(lang, "home"))
    home_alts = build_alternates("home", None, registry)
    for lang in LANGS:
        t = i18n[lang]
        rel = url_for(lang, "home")
        guides_list = []
        for g in guides_manifest["guides"]:
            ginfo = g[lang]
            guides_list.append(
                {
                    "title": ginfo["title"],
                    "url": url_for(lang, "article", g["slug"]),
                    "description": ginfo.get("description", ""),
                    "product": g.get("product"),
                }
            )
        html = env.get_template("home.html").render(
            lang=lang,
            t=t,
            title=t["home_meta_title"],
            description=t["home_meta_description"],
            site_url=SITE_URL,
            canonical=SITE_URL + rel,
            alternates=home_alts,
            products=products_data,
            guides_list=guides_list[:3],
            blog_url=url_for(lang, "blog"),
            page_type="home",
        )
        write_page(rel, html)

    # --- Products ---
    for product in products_data["products"]:
        pid = product["id"]
        for lang in LANGS:
            register(lang, "product", pid, url_for(lang, "product", pid))
        product_alts = build_alternates("product", pid, registry)
        for lang in LANGS:
            pdata = product[lang]
            rel = url_for(lang, "product", pid)
            related_guides = []
            for g in guides_manifest["guides"]:
                if g.get("product") == pid:
                    related_guides.append(
                        {
                            "title": g[lang]["title"],
                            "url": url_for(lang, "article", g["slug"]),
                        }
                    )
            if pid == "optimus":
                hub_slug = "paradojas-del-gaming"
                hub = next((g for g in guides_manifest["guides"] if g["slug"] == hub_slug), None)
                if hub:
                    hub_entry = {
                        "title": hub[lang]["title"],
                        "url": url_for(lang, "article", hub_slug),
                    }
                    related_guides = [hub_entry] + [
                        g for g in related_guides if hub_slug not in g["url"]
                    ]
            schema = {
                "@context": "https://schema.org",
                "@type": "SoftwareApplication",
                "name": product["name"],
                "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "Windows 10, Windows 11",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "publisher": {"@type": "Organization", "name": "Korelabs"},
                "downloadUrl": product["downloads"]["setup"],
                "description": pdata["meta_description"],
                "softwareVersion": product["version"],
                "inLanguage": lang,
            }
            html = env.get_template("product.html").render(
                lang=lang,
                t=i18n[lang],
                title=pdata["meta_title"],
                description=pdata["meta_description"],
                site_url=SITE_URL,
                canonical=SITE_URL + rel,
                alternates=product_alts,
                product=product,
                pdata=pdata,
                related_guides=related_guides[:4],
                faq_url=url_for(lang, "faq"),
                schema_json=json.dumps(schema, ensure_ascii=False),
                page_type="product",
            )
            write_page(rel, html)

    # --- FAQ ---
    for lang in LANGS:
        register(lang, "faq", None, url_for(lang, "faq"))
    faq_alts = build_alternates("faq", None, registry)
    for lang in LANGS:
        rel = url_for(lang, "faq")
        fdata = faq_data[lang]
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
                for section in fdata["sections"]
                for item in section["items"]
            ],
        }
        html = env.get_template("faq.html").render(
            lang=lang,
            t=i18n[lang],
            title=fdata["meta_title"],
            description=fdata["meta_description"],
            site_url=SITE_URL,
            canonical=SITE_URL + rel,
            alternates=faq_alts,
            fdata=fdata,
            schema_json=json.dumps(faq_schema, ensure_ascii=False),
            page_type="faq",
        )
        write_page(rel, html)

    # --- Blog (índice de artículos) ---
    product_labels = {"optimus": "Optimus", "coto": "Coto", "dicto": "Dicto"}
    for lang in LANGS:
        register(lang, "blog", None, url_for(lang, "blog"))
    blog_alts = build_alternates("blog", None, registry)
    for lang in LANGS:
        t = i18n[lang]
        rel = url_for(lang, "blog")
        articles = []
        for g in guides_manifest["guides"]:
            ginfo = g[lang]
            pid = g.get("product")
            articles.append(
                {
                    "title": ginfo["title"],
                    "description": ginfo.get("description", ""),
                    "url": url_for(lang, "article", g["slug"]),
                    "product": pid,
                    "product_label": product_labels.get(pid, "") if pid else "",
                }
            )
        blog_schema = {
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": t["blog_index_title"],
            "description": t["blog_meta_description"],
            "url": SITE_URL + rel,
            "publisher": {"@type": "Organization", "name": "Korelabs"},
            "inLanguage": lang,
        }
        html = env.get_template("blog.html").render(
            lang=lang,
            t=t,
            title=t["blog_meta_title"],
            description=t["blog_meta_description"],
            site_url=SITE_URL,
            canonical=SITE_URL + rel,
            alternates=blog_alts,
            articles=articles,
            schema_json=json.dumps(blog_schema, ensure_ascii=False),
            page_type="blog",
        )
        write_page(rel, html)

    # --- Artículos ---
    for g in guides_manifest["guides"]:
        slug = g["slug"]
        for lang in LANGS:
            register(lang, "article", slug, url_for(lang, "article", slug))
        article_alts = build_alternates("article", slug, registry)
        for lang in LANGS:
            rel = url_for(lang, "article", slug)
            ginfo = g[lang]
            md_path = CONTENT / "guides" / ginfo["file"]
            meta, body_html = parse_guide_md(md_path.read_text(encoding="utf-8"))
            body_html, toc = extract_toc(body_html)
            product_id = g.get("product")
            product_url = url_for(lang, "product", product_id) if product_id else None
            related = []
            for rs in g.get("related", []):
                for og in guides_manifest["guides"]:
                    if og["slug"] == rs:
                        related.append({"title": og[lang]["title"], "url": url_for(lang, "article", rs)})
            breadcrumbs = [
                {"name": i18n[lang]["nav_home"], "url": url_for(lang, "home")},
                {"name": i18n[lang]["nav_blog"], "url": url_for(lang, "blog")},
                {"name": ginfo["title"], "url": rel},
            ]
            article_schema = {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": ginfo["title"],
                "description": ginfo["description"],
                "author": {"@type": "Organization", "name": "Korelabs"},
                "publisher": {
                    "@type": "Organization",
                    "name": "Korelabs",
                    "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/assets/img/korelabs-logo.png"},
                },
                "dateModified": TODAY,
                "inLanguage": lang,
            }
            breadcrumb_schema = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": b["name"], "item": SITE_URL + b["url"]}
                    for i, b in enumerate(breadcrumbs)
                ],
            }
            html = env.get_template("guide.html").render(
                lang=lang,
                t=i18n[lang],
                site_url=SITE_URL,
                canonical=SITE_URL + rel,
                alternates=article_alts,
                title=ginfo["title"],
                description=ginfo["description"],
                body_html=body_html,
                toc=toc,
                breadcrumbs=breadcrumbs,
                product_url=product_url,
                product_name=g.get("product", "").capitalize() if product_id else None,
                related_guides=related[:2],
                faq_url=url_for(lang, "faq"),
                schema_article=json.dumps(article_schema, ensure_ascii=False),
                schema_breadcrumb=json.dumps(breadcrumb_schema, ensure_ascii=False),
                today=TODAY,
                page_type="guide",
            )
            write_page(rel, html)

    copy_static()
    write_redirects()
    write_robots()
    write_sitemaps(urls_by_lang)

    total = sum(len(v) for v in urls_by_lang.values())
    print(f"Built {total} pages -> {DIST}")
    index = DIST / "es" / "index.html"
    if total == 0 or not index.is_file():
        raise SystemExit(f"Build verification failed: missing output at {index}")


if __name__ == "__main__":
    main()
