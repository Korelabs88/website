# Korelabs Website — Hub SEO multilingüe

Sitio estático generado con Python + Jinja2. Idiomas: **ES**, **EN**, **PT**.

## Desarrollo local

```powershell
cd C:\Korelabs\website
pip install -r requirements.txt
python scripts/generate_guides.py   # solo si faltan guías
python scripts/build.py
```

Abre `dist/es/index.html` con un servidor local, o:

```powershell
cd dist && python -m http.server 8080
```

Visita http://localhost:8080/es/

## Estructura

```
content/          Datos (i18n, productos, FAQ, guías Markdown)
templates/        Plantillas Jinja2
scripts/build.py  Genera dist/
dist/             Output desplegado (no commitear)
```

## Cloudflare Pages

| Campo | Valor |
|-------|-------|
| Build command | `pip install -r requirements.txt && python scripts/generate_guides.py && python scripts/build.py` |
| Build output | `dist` |
| Python version | 3.12 |

## Añadir contenido

- **Producto:** editar `content/products.json` y rebuild
- **Guía:** añadir entrada en `content/guides/manifest.json` + archivo `.md` en 3 idiomas
- **UI:** editar `content/i18n/{es,en,pt}.json`

## SEO

- Sitemaps generados: `/sitemap.xml`, `/sitemap-{es,en,pt}.xml`
- Hreflang en cada página
- `/` redirige a `/es/` vía `_redirects`

Ver `docs/SEO-OFFPAGE.md` y `docs/SEO-MONITORING.md`.
