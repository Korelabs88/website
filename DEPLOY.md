# Publicar Korelabs en alexkore.com

Guía paso a paso para poner la landing online (gratis) y que aparezca en Google.

---

## Resumen de la arquitectura

```
alexkore.com (Porkbun)  ──►  Cloudflare Pages (hosting web gratis)
                                     │
Botón "Descargar"  ──────────►  GitHub Releases (aloja el instalador .exe)
```

- **Web (esta carpeta)** → Cloudflare Pages. Gratis, HTTPS, CDN global, ancho de banda ilimitado.
- **Instalador de Optimus** → GitHub Releases. Gratis y pensado para binarios pesados.

---

## Paso 1 — Subir la web a GitHub

1. Crea una cuenta en https://github.com (si no tienes).
2. Crea un repositorio nuevo, por ejemplo `website` dentro de la organización `Korelabs88`.
3. Sube el contenido de esta carpeta (`C:\Korelabs\website`). Desde una terminal aquí:

```powershell
cd C:\Korelabs\website
git init
git add .
git commit -m "Landing de Korelabs"
git branch -M main
git remote add origin https://github.com/Korelabs88/website.git
git push -u origin main
```

---

## Paso 2 — Conectar Cloudflare Pages

1. Crea una cuenta en https://dash.cloudflare.com (gratis).
2. Ve a **Workers & Pages → Create → Pages → Connect to Git**.
3. Elige el repo `Korelabs88/website`.
4. Configuración de build:
   - **Framework preset**: None
   - **Build command**: `pip install -r requirements.txt && python scripts/generate_guides.py && python scripts/build.py`
   - **Build output directory**: `dist`
   - **Environment variable** (opcional): `PYTHON_VERSION=3.12`
5. Deploy. Te dará una URL tipo `website.pages.dev` para probar.

> **Importante:** el directorio de salida (`dist`) **no debe estar en `.gitignore`**. Cloudflare Pages omite del deploy los archivos que coinciden con `.gitignore`, aunque el build sea exitoso. Si ves deploy "Success" pero todas las URLs dan 404, revisá esto primero.

> **Python:** añade variable de entorno `PYTHON_VERSION=3.12` en Settings → Environment variables.

> **Indexación:** en Settings → disable "Managed robots.txt" si sustituye tu `robots.txt`; activa "Allow search engine indexing" (sin `X-Robots-Tag: noindex`).

---

## Paso 3 — Conectar tu dominio alexkore.com

Tienes dos opciones. La más simple y potente:

### Opción A (recomendada): mover el dominio a Cloudflare
1. En Cloudflare: **Add a site → alexkore.com** (plan Free).
2. Cloudflare te dará **2 nameservers** (ej. `xxx.ns.cloudflare.com`).
3. Entra a **Porkbun → Details de alexkore.com → Authoritative Nameservers** y reemplázalos por los de Cloudflare.
4. Vuelve a **Pages → tu proyecto → Custom domains → Set up a domain** y añade `alexkore.com` y `www.alexkore.com`. Cloudflare crea los registros DNS solo.

### Opción B: dejar el DNS en Porkbun
1. En Pages copia el destino CNAME que te indica (`tu-proyecto.pages.dev`).
2. En **Porkbun → DNS** crea:
   - `CNAME` para `www` → `tu-proyecto.pages.dev`
   - Registro raíz (`ALIAS`/`ANAME`) para `alexkore.com` → `tu-proyecto.pages.dev`

El HTTPS se activa solo en unos minutos.

---

## Paso 4 — Alojar el instalador de Optimus

1. En GitHub crea un repo (puede ser privado el código, pero el Release debe ser público), ej. `optimus`.
2. Ve a **Releases → Draft a new release**, sube el instalador (`OptimusSetup.exe`) y publícalo.
3. La URL `https://github.com/Korelabs88/Optimus/releases/latest` siempre apunta a la última versión.
4. En `index.html`, ese enlace ya está apuntando a `Korelabs88/Optimus` en el botón de descarga.

---

## Paso 5 — Que aparezca en Google

1. Entra a https://search.google.com/search-console
2. Añade la propiedad **Dominio**: `alexkore.com` (verifica con un registro TXT en el DNS).
3. En **Sitemaps**, envía: `https://alexkore.com/sitemap.xml`
4. Usa **Inspección de URLs → Solicitar indexación** para acelerar.

En pocos días tu web aparecerá al buscar "Korelabs" o "Optimus" en Google.

---

## Solución de problemas

### Deploy "Success" pero URLs dan 404

1. **`.gitignore` no debe listar `dist/`** — Pages no sube archivos ignorados.
2. Tras corregir, **Retry deployment** en Cloudflare.
3. Verificá: `https://tu-proyecto.pages.dev/es/` debe dar **200** (no 404).
4. `https://tu-proyecto.pages.dev/robots.txt` debe contener `Sitemap: https://alexkore.com/sitemap.xml` (no el robots genérico de Cloudflare).

### Search Console rechaza indexación

- Casi siempre porque la URL devuelve **404** en la prueba en vivo.
- Arreglá el deploy primero; después reenviá el sitemap.

---

## Actualizar la web más adelante

1. Edita contenido en `content/` o plantillas en `templates/`.
2. Ejecuta localmente: `python scripts/build.py` (opcional, para previsualizar en `dist/`).
3. `git push` — Cloudflare reconstruye y despliega desde `dist/`.

Para añadir un programa: actualiza `content/products.json` y las traducciones en `content/i18n/`.

Para SEO off-page y métricas: ver `docs/SEO-OFFPAGE.md` y `docs/SEO-MONITORING.md`.
