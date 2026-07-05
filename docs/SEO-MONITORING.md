# Seguimiento SEO — Korelabs

Guía para medir progreso hacia página 1 en keywords objetivo.

## Herramientas

| Herramienta | Uso |
|-------------|-----|
| [Google Search Console](https://search.google.com/search-console) | Impresiones, clics, posición, indexación |
| [Bing Webmaster](https://www.bing.com/webmasters) | Tráfico adicional |
| Búsqueda manual `site:alexkore.com` | URLs indexadas |
| PageSpeed Insights | Core Web Vitals |

## Configuración inicial en Search Console

1. Propiedad: **alexkore.com** (dominio)
2. Sitemaps → Añadir: `https://alexkore.com/sitemap.xml`
3. Verificar que aparecen sitemaps `sitemap-es.xml`, `sitemap-en.xml`, `sitemap-pt.xml`

## KPIs — meta 90 días

| Métrica | Objetivo |
|---------|----------|
| URLs indexadas | 45+ (actual), crecer con nuevas guías |
| Impresiones/día | Tendencia ascendente |
| Posición media (long-tail) | < 20 en queries objetivo |
| CTR | > 3% en páginas con impresiones |
| Core Web Vitals | Todo verde |

## Keywords a monitorizar

### Marca (rápido)
- Korelabs
- Optimus Korelabs
- Dicto Korelabs
- alexkore.com

### Long-tail ES
- liberar ram windows gratis
- convertir pdf word offline
- transcribir audio whisper local

### Long-tail EN
- free ram cleaner windows
- offline pdf to word converter
- offline audio transcription whisper

### Long-tail PT
- liberar ram windows grátis
- converter pdf offline
- transcrever áudio localmente

## Revisión semanal (15 min)

1. **Rendimiento** → filtrar por país (España, USA, Brasil)
2. Anotar top 10 queries por impresiones
3. Para CTR < 2%: reescribir `meta_title` / `meta_description` en `content/`
4. Rebuild + deploy + solicitar reindexación solo si cambio importante

## Revisión mensual

1. Comparar impresiones mes a mes por idioma
2. Identificar guías sin impresiones → mejorar enlaces internos desde home/productos
3. Añadir 2–4 guías nuevas según queries reales en GSC
4. Comprobar enlaces rotos en landings

## Iteración de títulos

Plantilla que funciona:

```
{Keyword principal} — {Producto} | Korelabs
```

Ejemplo bajo CTR: probar variante con beneficio:

```
Antes: Liberar RAM en Windows gratis — Optimus | Korelabs
Después: Libera RAM standby en Windows 11 gratis | Optimus
```

Cambiar en `content/products.json` o frontmatter de guía → `python scripts/build.py` → deploy.

## Alertas

Revisar en GSC → Indexación → Páginas:

- **Excluidas** por canonical duplicado → revisar hreflang
- **Error 404** → corregir enlaces internos
- **Soft 404** → añadir contenido útil a la URL

## Registro de cambios SEO

| Fecha | Cambio | Resultado (2 sem después) |
|-------|--------|---------------------------|
| | Hub multilingüe 45 URLs | |
| | Sitemaps por idioma | |

Completar esta tabla tras cada deploy SEO relevante.
