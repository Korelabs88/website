## De video a subtítulos sin subir el archivo

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
