#!/usr/bin/env python3
"""Genera archivos Markdown de guías SEO (ejecutar una vez o al añadir guías)."""

from pathlib import Path

GUIDES = Path(__file__).resolve().parent.parent / "content" / "guides"

CONTENT = {
    "liberar-ram-windows.es.md": """## Por qué Windows se queda sin RAM

Windows gestiona la memoria de forma agresiva: retiene archivos y programas recientes en la **lista standby** para acelerar re-aperturas. Eso no es un error, pero cuando abres juegos o apps pesadas puedes quedarte corto de RAM disponible.

Muchos "optimizadores" muestran un porcentaje falso o liberan memoria que Windows recupera al instante. Lo que funciona es actuar sobre **working sets**, **standby** y **modified** con APIs nativas.

## Métodos que sí funcionan

### 1. Cerrar apps que no usas
El Administrador de tareas (Ctrl+Shift+Esc) muestra qué proceso consume más RAM. Cierra pestañas del navegador y apps en segundo plano antes de cualquier herramienta.

### 2. Revisar programas de inicio
Menos programas al arrancar = más RAM libre desde el minuto cero. Optimus incluye gestión de inicio integrada.

### 3. Liberación real con Optimus
**Optimus** ejecuta operaciones documentadas de Windows:

- Vaciar working sets de procesos
- Purgar lista standby (la más efectiva)
- Volcar páginas modified
- Vaciar caché de ficheros del sistema (opcional, requiere admin)

Mide antes y después con desglose de memoria. Sin telemetría ni suscripción.

## Qué evitar

- Programas que prometen "50% más RAM" con animaciones falsas
- Servicios online que piden acceso remoto a tu PC
- Desactivar la paginación sin saber qué haces

## Pasos recomendados

1. Descarga Optimus (instalador o portable)
2. Ejecuta como administrador para funciones avanzadas
3. Abre el módulo RAM y revisa standby/modified
4. Selecciona operaciones y confirma
5. Compara el resultado en el monitor en vivo

## Preguntas frecuentes

**¿Liberar RAM daña Windows?** No, si usas operaciones reversibles como las de Optimus.

**¿Cuánta RAM debería liberar?** Depende del sistema. Lo importante es recuperar standby real, no un número fijo.

**¿Es gratis?** Sí. Optimus es gratuito y local.
""",
    "liberar-ram-windows.en.md": """## Why Windows runs out of RAM

Windows manages memory aggressively: it keeps recent files and apps in the **standby list** to speed up re-launching. That's not a bug, but when you open games or heavy apps you may run short on available RAM.

Many "optimizers" show fake percentages or free memory Windows instantly reclaims. What works is targeting **working sets**, **standby** and **modified** with native APIs.

## Methods that actually work

### 1. Close unused apps
Task Manager (Ctrl+Shift+Esc) shows top RAM consumers. Close browser tabs and background apps before any tool.

### 2. Review startup programs
Fewer apps at boot = more free RAM from minute one. Optimus includes startup management.

### 3. Real freeing with Optimus
**Optimus** runs documented Windows operations:

- Empty process working sets
- Purge standby list (most effective)
- Flush modified pages
- Clear system file cache (optional, requires admin)

Measure before/after with memory breakdown. No telemetry or subscription.

## What to avoid

- Tools promising "50% more RAM" with fake animations
- Online services asking for remote PC access
- Disabling paging without knowing the impact

## Recommended steps

1. Download Optimus (installer or portable)
2. Run as administrator for advanced features
3. Open the RAM module and review standby/modified
4. Select operations and confirm
5. Compare results in the live monitor

## FAQ

**Does freeing RAM harm Windows?** Not with reversible operations like Optimus uses.

**How much RAM should I free?** It depends. Focus on real standby recovery, not a fixed number.

**Is it free?** Yes. Optimus is free and local.
""",
    "liberar-ram-windows.pt.md": """## Por que o Windows fica sem RAM

O Windows gere memória de forma agressiva: mantém arquivos e apps recentes na **lista standby** para abrir mais rápido. Não é erro, mas ao abrir jogos ou apps pesados você pode ficar sem RAM disponível.

Muitos "otimizadores" mostram porcentagem falsa ou liberam memória que o Windows recupera na hora. O que funciona é agir sobre **working sets**, **standby** e **modified** com APIs nativas.

## Métodos que funcionam

### 1. Fechar apps não usadas
O Gerenciador de Tarefas (Ctrl+Shift+Esc) mostra o que mais consome RAM.

### 2. Revisar programas de inicialização
Menos apps na boot = mais RAM livre desde o início. Optimus inclui gestão de inicialização.

### 3. Liberação real com Optimus
**Optimus** executa operações documentadas do Windows: esvaziar working sets, purgar standby, descarregar modified e limpar cache do sistema (opcional, admin).

Mede antes/depois com detalhamento. Sem telemetria ou assinatura.

## O que evitar

- Programas que prometem "50% mais RAM" com animações falsas
- Serviços online com acesso remoto ao PC

## Passos recomendados

1. Baixe Optimus
2. Execute como administrador se necessário
3. Abra o módulo RAM
4. Selecione operações e confirme
5. Compare no monitor ao vivo

## FAQ

**Liberar RAM prejudica o Windows?** Não, com operações reversíveis como as do Optimus.

**É grátis?** Sim. Optimus é gratuito e local.
""",
    "memoria-standby-windows.es.md": """## Qué es la memoria standby

La **lista standby** es RAM que Windows usa como caché de disco en memoria. Contiene datos de archivos y apps cerrados que podrían necesitarse de nuevo. Por eso el Administrador de tareas muestra "memoria disponible" alta pero apps nuevas fallan: la RAM está en standby, no libre.

## Standby vs libre vs modified

| Tipo | Significado |
|------|-------------|
| Libre | Lista para apps nuevas |
| Standby | Caché reutilizable, se puede purgar |
| Modified | Páginas modificadas pendientes de escribir |

Purgar standby es seguro: Windows vuelve a cargar datos desde disco si hacen falta.

## Cómo liberar standby

1. Reiniciar el PC (drástico pero efectivo)
2. Usar **Optimus** → purgar lista standby con medición antes/después
3. Evitar herramientas que solo muestran gráficos bonitos

Optimus muestra standby, modified, compresión y total en una sola vista.

## Cuándo tiene sentido purgar

- Antes de un juego pesado o renderizado
- Cuando el sistema va lento tras horas de uso
- Tras cerrar apps que consumieron mucha RAM

No hace falta purgar cada hora: Windows gestiona bien la memoria en uso normal.

## Conclusión

Entender standby te evita "optimizadores" fraudulentos. Optimus libera memoria real con operaciones nativas, gratis y sin nube.
""",
    "memoria-standby-windows.en.md": """## What is standby memory

The **standby list** is RAM Windows uses as in-memory disk cache. It holds data from closed files and apps that might be needed again. Task Manager may show high "available" memory while new apps struggle because RAM is in standby, not truly free.

## Standby vs free vs modified

| Type | Meaning |
|------|---------|
| Free | Ready for new apps |
| Standby | Reusable cache, can be purged |
| Modified | Dirty pages pending write |

Purging standby is safe: Windows reloads from disk if needed.

## How to free standby

1. Reboot ( drastic but works )
2. Use **Optimus** → purge standby list with before/after metrics
3. Avoid tools that only show pretty charts

Optimus shows standby, modified, compression and totals in one view.

## When to purge

- Before heavy gaming or rendering
- When the system feels slow after hours of use
- After closing RAM-heavy apps

You don't need to purge hourly: Windows handles normal use well.

## Conclusion

Understanding standby helps you avoid fake optimizers. Optimus frees real memory with native operations, free and offline.
""",
    "memoria-standby-windows.pt.md": """## O que é memória standby

A **lista standby** é RAM que o Windows usa como cache em memória. Contém dados de arquivos e apps fechados que podem ser reutilizados. Por isso o Gerenciador de Tarefas mostra memória "disponível" alta mas apps novas falham.

## Standby vs livre vs modified

- **Livre**: pronta para novas apps
- **Standby**: cache reutilizável, pode ser purgada
- **Modified**: páginas sujas pendentes de gravação

Purgar standby é seguro: o Windows recarrega do disco se necessário.

## Como liberar standby

Use **Optimus** para purgar a lista standby com medição antes/depois. Evite ferramentas que só mostram gráficos.

## Conclusão

Entender standby evita otimizadores falsos. Optimus libera memória real, grátis e local.
""",
    "optimizar-windows-gaming.es.md": """## Objetivo: más FPS y menos stuttering

Optimizar Windows para gaming no es misterio: menos procesos compitiendo por CPU/RAM/disco y configuración coherente del sistema.

## Checklist antes de jugar

1. **Cierra apps en segundo plano** — Discord, navegador, grabadoras cloud
2. **Libera RAM standby** — Optimus purga caché retenida
3. **Revisa inicio de Windows** — desactiva lo innecesario
4. **Modo energía** — plan Alto rendimiento o Ultimate en portátiles enchufados
5. **Actualiza drivers GPU** — desde el fabricante, no solo Windows Update

## Modo Gamer de Optimus

Optimus incluye **Modo Gamer** que prioriza recursos para la sesión de juego: reduce ruido de fondo del sistema y prepara el PC antes de lanzar el título.

Combínalo con liberación de RAM y monitor en vivo para ver impacto.

## Qué no esperar

- No sustituye más RAM física ni una GPU mejor
- No overclockea hardware
- No desactiva antivirus de forma peligrosa

## Hardware vs software

| Mejora | Impacto |
|--------|---------|
| Más RAM | Alto si estabas al límite |
| SSD para juegos | Medio en tiempos de carga |
| Optimus + modo gamer | Medio en picos de stutter |

## Descarga

Optimus es gratis para Windows 10/11. Instalador o portable, sin cuenta.
""",
    "optimizar-windows-gaming.en.md": """## Goal: more FPS, less stuttering

Optimizing Windows for gaming means fewer processes competing for CPU/RAM/disk and sensible system settings.

## Pre-game checklist

1. **Close background apps** — browser, cloud recorders
2. **Free standby RAM** — Optimus purges retained cache
3. **Review startup** — disable unnecessary items
4. **Power plan** — High performance when plugged in
5. **Update GPU drivers** — from vendor site

## Optimus Game Mode

**Game Mode** prioritizes resources for your session: less background noise and a prepared system before launch.

Pair with RAM freeing and live monitoring.

## What not to expect

- Won't replace more physical RAM or a better GPU
- Won't unsafe-disable antivirus

## Download

Optimus is free for Windows 10/11. Installer or portable, no account.
""",
    "optimizar-windows-gaming.pt.md": """## Objetivo: mais FPS e menos stutter

Otimizar Windows para jogos significa menos processos competindo por CPU/RAM/disco.

## Checklist antes de jogar

1. Feche apps em segundo plano
2. Libere RAM standby com Optimus
3. Revise inicialização do Windows
4. Plano de energia: Alto desempenho
5. Atualize drivers da GPU

## Modo Gamer do Optimus

Prioriza recursos para a sessão de jogo. Combine com liberação de RAM e monitor ao vivo.

## Download

Optimus é grátis para Windows 10/11.
""",
    "optimus-vs-wise-memory-optimizer.es.md": """## Dos enfoques distintos

**Wise Memory Optimizer** es conocido por liberación rápida de RAM con un clic. **Optimus** es un optimizador completo: RAM, CPU, disco, inicio, servicios y modo gamer.

## Comparativa

| Criterio | Optimus | Wise Memory Optimizer |
|----------|---------|----------------------|
| Precio | Gratis | Gratis con extras de pago |
| Privacidad | Local, sin telemetría | Revisar política actual |
| Liberación RAM | Standby, working sets, modified | Principalmente RAM |
| Monitor hardware | Sí, integrado | Limitado |
| Limpieza disco | Sí | No |
| Modo gamer | Sí | No |
| Código / estudio | Korelabs, open releases | WiseCleaner |

## Cuándo elegir Optimus

- Quieres **una suite** en lugar de solo RAM
- Priorizas **privacidad** y software sin suscripción
- Necesitas ver **standby/modified** con detalle

## Cuándo Wise puede bastar

- Solo quieres un botón ocasional de "liberar memoria"
- No te importa funciones extra de pago

## Veredicto honesto

Wise cumple para usuarios casuales. Optimus apunta a quien quiere control real del sistema, gratis y local. Prueba Optimus — no hay registro ni coste oculto.
""",
    "optimus-vs-wise-memory-optimizer.en.md": """## Two different approaches

**Wise Memory Optimizer** is known for one-click RAM freeing. **Optimus** is a full optimizer: RAM, CPU, disk, startup, services and game mode.

## Comparison

| Criteria | Optimus | Wise Memory Optimizer |
|----------|---------|----------------------|
| Price | Free | Free with paid extras |
| Privacy | Local, no telemetry | Check current policy |
| RAM freeing | Standby, working sets, modified | Mainly RAM |
| Hardware monitor | Yes, built-in | Limited |
| Disk cleanup | Yes | No |
| Game mode | Yes | No |

## When to pick Optimus

- You want a **suite**, not just RAM
- You prioritize **privacy** and no subscription
- You need **standby/modified** detail

## Honest verdict

Wise works for casual users. Optimus targets people who want real system control, free and local.
""",
    "optimus-vs-wise-memory-optimizer.pt.md": """## Duas abordagens

**Wise Memory Optimizer** é conhecido por liberação rápida de RAM. **Optimus** é otimizador completo: RAM, CPU, disco, inicialização e modo gamer.

## Comparativo

| Critério | Optimus | Wise |
|----------|---------|------|
| Preço | Grátis | Grátis com extras pagos |
| Privacidade | Local | Ver política |
| RAM | Standby, working sets | Principalmente RAM |
| Monitor | Integrado | Limitado |

## Veredicto

Wise serve para uso casual. Optimus é para quem quer controle real, grátis e local.
""",
    "convertir-pdf-word-offline.es.md": """## Riesgo de los conversores online

Subir un PDF a un sitio web implica:

- Copia del documento en servidores desconocidos
- Posible retención según política de privacidad
- Límites de tamaño y páginas en planes gratis
- Marcas de agua o paywall

Para contratos, facturas o datos médicos, **offline es la opción sensata**.

## Convertir PDF a Word en local con Coto

**Coto** convierte PDF ↔ Word en tu PC:

1. Abre Coto e importa el PDF
2. Elige salida DOCX
3. Espera la cola local — nada se sube
4. Edita el Word resultante

## Calidad de conversión

PDF escaneado (imagen) requiere **OCR** primero — Coto lo incluye multiidioma. PDF nativo con texto seleccionable convierte mejor.

## Por lotes

Varios PDF a la vez: arrastra carpeta, define formato de salida, procesa cola completa.

## Alternativas cloud vs Coto

| | Cloud | Coto |
|---|-------|------|
| Privacidad | Baja | Alta |
| Offline | No | Sí |
| Coste | Suscripción | Gratis |

Descarga Coto gratis para Windows 10/11.
""",
    "convertir-pdf-word-offline.en.md": """## Risk of online converters

Uploading a PDF means copies on unknown servers, retention policies, size limits and watermarks. For contracts or medical data, **offline makes sense**.

## Convert PDF to Word locally with Coto

**Coto** converts PDF ↔ Word on your PC:

1. Open Coto and import the PDF
2. Choose DOCX output
3. Wait for local queue — nothing uploaded
4. Edit the resulting Word file

## Scanned PDFs

Scanned PDFs need **OCR** first — Coto includes multilingual OCR.

## Batch

Drop a folder, set output format, process the full queue.

## Cloud vs Coto

| | Cloud | Coto |
|---|-------|------|
| Privacy | Low | High |
| Offline | No | Yes |
| Cost | Subscription | Free |

Download Coto free for Windows 10/11.
""",
    "convertir-pdf-word-offline.pt.md": """## Risco de conversores online

Enviar PDF para servidores desconhecidos é risco para contratos e dados sensíveis. **Offline é sensato.**

## Converter PDF para Word com Coto

**Coto** converte PDF ↔ Word no seu PC sem upload. PDF escaneado precisa de **OCR** — Coto inclui OCR multilíngue.

## Lote

Arraste pasta, defina saída, processe fila local.

Baixe Coto grátis para Windows 10/11.
""",
    "ocr-pdf-offline.es.md": """## Qué es OCR offline

OCR (Reconocimiento Óptico de Caracteres) convierte imágenes de texto en texto editable. **Offline** significa que el motor corre en tu CPU/GPU — el archivo nunca sale del disco.

## Casos de uso

- Facturas escaneadas
- Libros PDF sin capa de texto
- Capturas de pantalla con texto
- Documentos en papel digitalizados

## OCR con Coto

1. Importa PDF o imagen (PNG, JPG, TIFF)
2. Selecciona idioma del documento
3. Coto procesa localmente
4. Exporta TXT, Word o PDF con capa de texto

## Precisión

Mejor con escaneos nítidos, 300 DPI mínimo recomendado. Documentos manuscritos siguen siendo difíciles para cualquier OCR.

## Privacidad

Servicios cloud de OCR entrenan modelos con tus datos. Coto no sube archivos — ideal para legal, salud y RRHH.

## FAQ

**¿Funciona sin internet?** Sí, tras instalar Coto.

**¿Multiidioma?** Sí, varios idiomas en un mismo flujo de trabajo.
""",
    "ocr-pdf-offline.en.md": """## What is offline OCR

OCR turns text images into editable text. **Offline** means the engine runs on your CPU/GPU — files never leave disk.

## Use cases

- Scanned invoices
- Image-only PDFs
- Screenshots with text

## OCR with Coto

1. Import PDF or image
2. Pick document language
3. Coto processes locally
4. Export TXT, Word or searchable PDF

## Privacy

Cloud OCR may use your data for training. Coto doesn't upload files.

## FAQ

**Works offline?** Yes, after installing Coto.

**Multilingual?** Yes.
""",
    "ocr-pdf-offline.pt.md": """## O que é OCR offline

OCR converte imagens de texto em texto editável no seu PC, sem upload.

## OCR com Coto

Importe PDF ou imagem, escolha idioma, processe localmente, exporte TXT ou Word.

## Privacidade

Coto não envia arquivos — ideal para legal, saúde e RH.
""",
    "unir-comprimir-pdf-local.es.md": """## Unir PDF sin servicios online

Combinar varios PDF en uno solo es tarea común: informes, escaneos por partes, anexos. Los sitios web piden subir todos los archivos — **Coto lo hace en local**.

### Pasos para unir

1. Abre herramientas PDF en Coto
2. Añade PDF en el orden deseado
3. Genera un solo archivo
4. Guarda en la carpeta que elijas

## Comprimir PDF

Archivos escaneados pesan mucho. Compresión local reduce tamaño para email sin perder legibilidad razonable.

| Acción | Cloud típico | Coto |
|--------|--------------|------|
| Unir | Upload múltiple | Local |
| Comprimir | Límite 25 MB | Sin límite artificial |
| Privacidad | Media | Alta |

## Proteger con contraseña

Coto también permite proteger PDF — todo offline.

Descarga Coto gratis para Windows.
""",
    "unir-comprimir-pdf-local.en.md": """## Merge PDF without online services

Combining PDFs is common for reports and scans. Web tools require uploads — **Coto does it locally**.

### Merge steps

1. Open PDF tools in Coto
2. Add PDFs in order
3. Generate single file
4. Save locally

## Compress PDF

Scanned files are heavy. Local compression reduces size for email.

## Password protect

Coto can protect PDFs — all offline.

Download Coto free for Windows.
""",
    "unir-comprimir-pdf-local.pt.md": """## Unir PDF sem serviços online

**Coto** combina e comprime PDF localmente, sem upload nem limites artificiais de tamanho.

Proteja PDF com senha — tudo offline.

Baixe Coto grátis para Windows.
""",
    "transcribir-audio-whisper-local.es.md": """## Por qué Whisper local

OpenAI Whisper es uno de los mejores motores open-source de transcripción. **faster-whisper** lo hace viable en PC de escritorio sin GPU enterprise.

Servicios como Otter o Rev cobran por minuto y almacenan audio en la nube. **Dicto** procesa en tu equipo.

## Formatos soportados

- Audio: MP3, WAV, M4A, FLAC, OGG
- Video: MP4, MKV, AVI (extrae audio con FFmpeg incluido)

## Flujo con Dicto

1. Instala Dicto (FFmpeg incluido)
2. Arrastra archivo o carpeta
3. Elige modelo: tiny (rápido) → medium (preciso)
4. Idioma auto o fijo
5. Exporta TXT, SRT, VTT o DOCX

## Hardware

| Modelo | RAM | GPU |
|--------|-----|-----|
| tiny | 4 GB | Opcional |
| base | 6 GB | Recomendada |
| medium | 8+ GB | Recomendada |

## Privacidad

Reuniones internas, pacientes, abogados: la transcripción no debe salir del disco. Dicto cumple.

Descarga Dicto gratis para Windows 10/11.
""",
    "transcribir-audio-whisper-local.en.md": """## Why local Whisper

Whisper is a top open-source transcription engine. **faster-whisper** makes it viable on desktop PCs.

Cloud services charge per minute and store audio. **Dicto** runs on your machine.

## Supported formats

Audio: MP3, WAV, M4A. Video: MP4, MKV (FFmpeg included).

## Dicto workflow

1. Install Dicto
2. Drop file or folder
3. Pick model: tiny → medium
4. Auto or fixed language
5. Export TXT, SRT, VTT or DOCX

## Privacy

Internal meetings, healthcare, legal — transcription shouldn't leave disk. Dicto delivers.

Download Dicto free for Windows 10/11.
""",
    "transcribir-audio-whisper-local.pt.md": """## Por que Whisper local

Whisper é motor open-source de transcrição. **Dicto** usa faster-whisper no seu PC, sem nuvem.

## Fluxo com Dicto

Arraste áudio/vídeo, escolha modelo, exporte TXT, SRT, VTT ou DOCX. FFmpeg incluído.

## Privacidade

Reuniões e dados sensíveis não devem sair do disco.

Baixe Dicto grátis para Windows 10/11.
""",
    "generar-srt-video-offline.es.md": """## De video a subtítulos sin subir el archivo

YouTube, aulas online y podcasts necesitan SRT/VTT. Los servicios cloud tienen límites de minutos y retención de contenido.

**Dicto** transcribe video localmente y exporta subtítulos listos para editores.

## Proceso

1. Importa MP4/MKV en Dicto
2. FFmpeg extrae pista de audio automáticamente
3. Whisper genera segmentos con timestamps
4. Exporta **SRT** o **VTT**

## Edición posterior

Abre SRT en VLC, Premiere, DaVinci o YouTube Studio. Ajusta tiempos si hace falta.

## Calidad

- Audio claro = mejor sync
- Ruido de fondo: usa modelo medium si tu PC aguanta
- Múltiples hablantes: revisa manualmente tras auto-transcripción

## vs servicios cloud

| | Cloud | Dicto |
|---|-------|-------|
| Límite minutos | Sí | No |
| Privacidad | Baja | Total |
| Coste | Suscripción | Gratis |

Descarga Dicto para Windows.
""",
    "generar-srt-video-offline.en.md": """## Video to subtitles without upload

Courses and podcasts need SRT/VTT. Cloud services have minute limits and retention policies.

**Dicto** transcribes video locally and exports ready subtitles.

## Process

1. Import MP4/MKV in Dicto
2. FFmpeg extracts audio
3. Whisper generates timed segments
4. Export **SRT** or **VTT**

## Quality tips

Clear audio = better sync. Use medium model if hardware allows.

## vs cloud

| | Cloud | Dicto |
|---|-------|-------|
| Minute limits | Yes | No |
| Privacy | Low | Full |
| Cost | Subscription | Free |

Download Dicto for Windows.
""",
    "generar-srt-video-offline.pt.md": """## Vídeo para legendas sem upload

**Dicto** transcreve vídeo localmente e exporta SRT/VTT. FFmpeg incluído, sem limite de minutos na nuvem.

Baixe Dicto para Windows.
""",
    "alternativa-local-otter-rev.es.md": """## Otter.ai y Rev: modelo de suscripción

**Otter.ai** y **Rev** son referentes en transcripción cloud:

- Cobran por minuto o plan mensual
- Subes audio/video a sus servidores
- Dependes de internet y políticas de retención

Funcionan bien para equipos que aceptan la nube. No son ideales para confidencialidad estricta.

## Dicto: Whisper en tu PC

**Dicto** usa faster-whisper offline:

- Sin cuota mensual
- Sin upload de archivos
- Exporta TXT, SRT, VTT, DOCX
- Cola por lotes para carpetas enteras

## Comparativa rápida

| | Otter/Rev | Dicto |
|---|-----------|-------|
| Precio | Suscripción | Gratis |
| Offline | No | Sí |
| Privacidad | Cloud | Local |
| GPU opcional | N/A | Sí |

## Cuándo usar cloud

- Colaboración en tiempo real con varios editores
- Integraciones enterprise ya contratadas

## Cuándo Dicto gana

- Entrevistas sensibles
- Sin presupuesto recurrente
- PC potente y muchos archivos por procesar

Prueba Dicto gratis — Windows 10/11, portable disponible.
""",
    "alternativa-local-otter-rev.en.md": """## Otter.ai and Rev: subscription model

Cloud leaders charge monthly or per minute. You upload media to their servers.

**Dicto** runs faster-whisper offline: no quota, no upload, exports TXT/SRT/VTT/DOCX, batch queue.

## Quick compare

| | Otter/Rev | Dicto |
|---|-----------|-------|
| Price | Subscription | Free |
| Offline | No | Yes |
| Privacy | Cloud | Local |

## When Dicto wins

Sensitive interviews, no recurring budget, batch processing on your PC.

Try Dicto free — Windows 10/11.
""",
    "alternativa-local-otter-rev.pt.md": """## Otter.ai e Rev vs Dicto

Serviços cloud cobram assinatura e armazenam áudio. **Dicto** usa Whisper offline: grátis, sem upload, exporta TXT/SRT/VTT/DOCX.

Ideal para entrevistas sensíveis e processamento em lote.

Experimente Dicto grátis — Windows 10/11.
""",
}


def main() -> None:
    GUIDES.mkdir(parents=True, exist_ok=True)
    for name, body in CONTENT.items():
        path = GUIDES / name
        if not path.exists():
            path.write_text(body.strip() + "\n", encoding="utf-8")
            print(f"Created {name}")
        else:
            print(f"Skip {name} (exists)")


if __name__ == "__main__":
    main()
