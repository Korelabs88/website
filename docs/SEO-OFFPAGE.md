# Plan off-page SEO — Korelabs

Checklist de distribución para ganar autoridad de dominio. Ejecutar en paralelo al hub web.

## Serie estrella: Paradojas del gaming (16 artículos)

Hub principal — **prioridad de indexación y distribución**:

| Idioma | URL |
|--------|-----|
| ES | https://alexkore.com/es/blog/paradojas-del-gaming/ |
| EN | https://alexkore.com/en/blog/paradojas-del-gaming/ |
| PT | https://alexkore.com/pt/blog/paradojas-del-gaming/ |

Cierre de serie: `/es/blog/entender-hardware-disfrutar-menos-paradoja/`

### Indexación inmediata (Search Console + Bing)

- [ ] Reenviar sitemap: `https://alexkore.com/sitemap.xml`
- [ ] Inspeccionar e indexar:
  - Hub paradojas (ES, EN, PT)
  - Cierre #16 (ES, EN, PT)
  - Top 5 por impresiones potencial: `compraste-gpu-equivocada`, `fps-promedio-vs-fluidez`, `ram-no-esta-llena-standby`, `dlss-fsr-mejor-que-nativo`, `144hz-percepcion-vs-habilidad-paradoja`
- [ ] Verificar: `site:alexkore.com paradojas del gaming`

### On-site (hecho / mantener)

- [x] Landings Optimus enlazan al hub (sección + sidebar)
- [ ] Guías técnicas RAM/Windows enlazan a paradojas relevantes (próximo paso opcional)

## GitHub (prioridad alta)

- [ ] **Optimus** README: enlace a `https://alexkore.com/es/optimus/` (y `/en/`, `/pt/`)
- [ ] **Optimus** README: sección "Guías" con link al hub paradojas
- [ ] **Coto** README: enlace a `https://alexkore.com/es/coto/`
- [ ] **Dicto** README: enlace a `https://alexkore.com/es/dicto/`
- [ ] Perfil org **Korelabs88**: URL del sitio en bio
- [ ] Releases: descripción con enlace a landing del producto, no solo al .exe

## Comunidades gaming (sin spam)

Publicar contenido útil, no solo enlaces. Adaptar tono al subreddit.

### Reddit — serie paradojas

- [ ] **r/pcmasterrace** — post: *"16 paradoxes about why your PC doesn't perform like marketing promised"* → hub EN o ES según reglas del sub
- [ ] **r/buildapc** — comentar threads de "should I upgrade GPU?" citando artículo #1 (GPU equivocada) + hub
- [ ] **r/Windows11** — artículo RAM standby (#2) o debloat (#9) con link a guía concreta
- [ ] **r/GlobalOffensive**, **r/valorant** — 144Hz (#7) o 1% low (#5) solo si el thread lo pide

Plantilla de post (ES, adaptar):

> Llevamos meses escribiendo una serie sobre paradojas del gaming en PC: GPU, RAM, DLSS, ray tracing, streaming, etc. No es lista de specs — es por qué gastamos mal y medimos de más. Índice: [link hub ES]

### Reddit — producto Optimus

- [ ] r/Windows10, r/Windows11 — guía RAM / optimización con enlace a `/es/blog/liberar-ram-windows/` o hub paradojas
- [ ] r/software, r/selfhosted — privacidad local (Coto, Dicto)

### Foros ES/PT

- [ ] Foros hardware (HardForum ES, etc.) — responder con artículo relevante, no copy-paste del hub entero
- [ ] Comunidades Discord gaming — compartir 1 artículo por semana, no spam del índice

## Search Console y Bing

- [ ] Enviar sitemap índice: `https://alexkore.com/sitemap.xml`
- [ ] Inspeccionar e indexar landings clave:
  - `/es/optimus/`, `/en/optimus/`, `/pt/optimus/`
  - `/es/coto/`, `/es/dicto/`
  - Hub paradojas + 3–5 guías principales por idioma
- [ ] Registrar en [Bing Webmaster Tools](https://www.bing.com/webmasters) y enviar el mismo sitemap

## Video

- [ ] YouTube: *"5 paradojas que te hacen gastar mal en PC"* (Short) → hub en descripción
- [ ] YouTube: demo Optimus (liberar RAM) — descripción con `/es/optimus/` + link paradojas RAM
- [ ] YouTube: demo Coto (PDF offline)
- [ ] YouTube: demo Dicto (Whisper local)

## Directorios

- [ ] [AlternativeTo](https://alternativeto.net/) — fichas Optimus, Coto, Dicto (descripción con link al blog)
- [ ] Product Hunt — lanzamiento suite Korelabs (cuando haya tracción)

## Prensa / blogs

- [ ] Contactar blogs gaming / hardware ES, EN, PT — pitch: serie paradojas como guest resource
- [ ] Guest post sobre privacidad en conversión PDF o transcripción local (Coto/Dicto)

## Post de cierre (redes)

Copiar/pegar cuando quieras anunciar la serie completa:

**ES:** *Serie completa: 16 paradojas del gaming en PC — de la GPU equivocada a por qué saber demasiado de hardware arruina el disfrute. Índice: https://alexkore.com/es/blog/paradojas-del-gaming/*

**EN:** *Full series: 16 PC gaming paradoxes — from the wrong GPU to why knowing too much about hardware kills the fun. Index: https://alexkore.com/en/blog/paradojas-del-gaming/*

## Evitar

- Comprar enlaces
- Spam de comentarios con link al hub en threads irrelevantes
- Traducciones automáticas sin revisar
- Keyword stuffing en posts
- Publicar los 16 artículos como 16 posts separados el mismo día

## Cadencia sugerida (post-serie)

| Semana | Acción |
|--------|--------|
| 1 | Indexar hub + cierre · GitHub READMEs · 1 post Reddit (hub) |
| 2 | 2 comentarios útiles en r/buildapc / r/pcmasterrace · Bing Webmaster |
| 3 | YouTube Short paradojas · AlternativeTo Optimus |
| 4 | Revisar GSC: queries gaming · ajustar titles si CTR < 2% |
| Mensual | 1 guía técnica nueva × 3 idiomas **o** iterar meta de artículos con impresiones |

La serie paradojas está **cerrada en 16 artículos**. Nuevo contenido: guías Optimus según datos reales de Search Console (ver `SEO-MONITORING.md`).
