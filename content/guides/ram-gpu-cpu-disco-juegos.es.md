## Respuesta rápida: ¿quién manda en qué?

| Componente | Afecta sobre todo a… | Impacto típico en partida |
|------------|----------------------|---------------------------|
| **GPU** | FPS, calidad gráfica, resolución | **Muy alto** |
| **CPU** | FPS mínimos, simulaciones, multitud de NPCs | **Alto** (depende del juego) |
| **RAM** | Stuttering, cierres, multitarea (Discord + juego) | **Medio** (si hay poca o está llena) |
| **Disco** | Tiempos de carga, streaming de texturas | **Bajo en FPS**; **alto en cargas** |

No hay un solo "rey": un juego competitivo en 1080p puede estar limitado por la CPU; uno AAA en 4K, por la GPU; y si tienes 8 GB de RAM llenos, todo patina aunque la gráfica sea buena.

## GPU: el motor de los fotogramas

La **tarjeta gráfica** dibuja cada frame: shaders, texturas, rayos, postprocesado. En la mayoría de juegos modernos en 1440p o 4K, la GPU es el **primer cuello de botella** si quieres subir calidad visual o FPS.

### Qué mira en la GPU

- **VRAM** (memoria de vídeo): 8 GB suele bastar en 1080p/1440p con ajustes razonables; 12–16 GB dan margen en 4K y mods pesados. Si se llena, stuttering y bajadas bruscas de FPS.
- **Potencia bruta** (shader cores): define cuántos FPS aguantas a X resolución.
- **Drivers actualizados**: a veces +10 % solo con instalar la versión del fabricante (NVIDIA/AMD/Intel).

### Señales de que la GPU es el límite

- Uso de GPU ~95–100 % en partida y CPU más baja
- Bajar resolución o calidad **sube mucho** los FPS
- Herramientas como MSI Afterburner muestran GPU al límite y CPU con margen

**Optimus** no sustituye una GPU mejor, pero el **modo gamer** y liberar RAM ayudan a que la CPU alimente a la gráfica sin procesos basura compitiendo.

## CPU: el director de orquesta

El **procesador** prepara la escena: física, IA, animaciones, llamadas al motor gráfico. Juegos **single-thread** (pocos núcleos muy rápidos) dependen mucho de la velocidad de un núcleo; estrategia, MMO y simuladores usan **más núcleos**.

### Cuándo la CPU limita más que la GPU

- Shooters competitivos a **1080p alto FPS** (CS2, Valorant, Fortnite)
- Ciudades densas en **Cyberpunk**, **Starfield**, **Cities: Skylines**
- Emulación, Minecraft con muchos mods, servidores locales

### Señales de cuello de botella en CPU

- GPU al 60–70 % y **un núcleo** de CPU al 100 %
- FPS mínimos (1 % lows) muy malos aunque la media sea aceptable
- Subir calidad gráfica **casi no baja** FPS (ya no es la GPU)

Más núcleos no siempre ayudan: muchos títulos siguen usando 4–6 núcleos de forma intensa. Importan **GHz**, arquitectura reciente y latencia memoria.

## RAM: capacidad, velocidad y "memoria llena"

La **RAM** guarda el juego, texturas en tránsito, Discord, navegador, antivirus y el propio Windows. No dibuja frames como la GPU, pero **sin RAM libre** el sistema usa disco (paging) y aparecen **microcortes** (stutter).

### Capacidad recomendada (2026)

| Uso | RAM mínima cómoda |
|-----|-------------------|
| Juegos casuales + Windows | 16 GB |
| AAA + Discord + navegador | **32 GB** |
| 4K, mods, streaming local | 32–64 GB |

Con **8 GB** hoy muchos títulos van justos o directamente no arrancan bien.

### Velocidad DDR (MT/s)

- DDR4 3200 vs 3600: diferencia **pequeña** en FPS (1–5 % en muchos juegos)
- DDR5 5600+: algo más de margen en CPU con iGPU o títulos sensibles a ancho de banda
- Lo crítico suele ser **tener suficiente**, no exprimir los últimos MHz

### RAM llena vs standby

Windows retiene datos en **lista standby** (caché). Eso es normal, pero antes de una sesión larga conviene:

- Cerrar pestañas y launchers que no uses
- Purgar standby si vas justo (**Optimus** lo hace con operaciones nativas y muestra before/after)

### Señales de problema de RAM

- Uso constante **>90 %** con disco activo
- Cierres inesperados ("memoria insuficiente")
- Stuttering en open world al moverte rápido, con GPU no saturada

## Disco: HDD, SATA SSD y NVMe

El **almacenamiento** casi no cambia FPS **en combate estable** una vez cargada la escena. Donde se nota:

| Tipo | Tiempo de carga | Streaming de mundo abierto | FPS en combate |
|------|-----------------|----------------------------|----------------|
| **HDD** | Lento, texturas tardías | Pops y stutter al girar | Igual que SSD* |
| **SATA SSD** | Rápido | Muy bueno | Referencia |
| **NVMe Gen4/5** | Muy rápido | Excelente en juegos que streaman assets | ~igual que SATA SSD en FPS |

\*En HDD algunos juegos **sí** stutterean en open world por no leer texturas a tiempo; no es "menos FPS teórico", es **hitches**.

### Qué hacer con el disco

- Instala el juego en **SSD** (idealmente NVMe si la placa lo tiene)
- Deja **20 %+ libre** en el disco del sistema: Windows y shaders cachean ahí
- Limpia temporales y cachés viejos (**Optimus** incluye limpieza profunda reversible)

No compres un NVMe Gen5 solo por +3 FPS; compáralo si odias esperar en pantallas de carga o juegas títulos que streaman mapas enormes (Flight Simulator, algunos RPG).

## Cómo interactúan los cuatro

Imagina un pipeline:

```
Disco → carga nivel y texturas en RAM
RAM → CPU prepara lógica y envía trabajo a GPU
CPU → ordena draw calls
GPU → pinta el frame
```

Si el **disco** es lento, el pipeline empieza tarde (cargas largas, pops).
Si la **RAM** falta, todo se atasca leyendo del SSD como si fuera RAM lenta.
Si la **CPU** no llega, la GPU espera (FPS bajos con GPU ociosa).
Si la **GPU** es débil, la CPU termina pronto y la gráfica sufre (FPS bajos con GPU al 100 %).

## ¿Qué mejorar primero?

Depende de tu síntoma:

| Síntoma | Prioridad probable |
|---------|-------------------|
| FPS bajos en 4K / ultra | GPU |
| FPS inestables en 1080p competitivo | CPU (y RAM si <16 GB) |
| Cargas eternas, texturas tardías | SSD / NVMe |
| Microcortes, alt+tab lento, cierres | RAM (más GB o liberar) |
| Todo va mal en un PC viejo | Plataforma completa (CPU+placa+RAM+Disco) |

Orden típico en un PC equilibrado **nuevo**: GPU ≥ CPU ≥ 32 GB RAM ≥ NVMe. En un PC ya montado, **mide** antes de gastar (Administrador de tareas, Afterburner, Optimus).

## Ajustes de software (gratis)

Antes de comprar hardware:

1. **Drivers GPU** al día
2. **Modo alto rendimiento** en Windows (enchufado en portátil)
3. Cerrar overlays y grabadores que no uses
4. **Modo gamer de Optimus** + liberar RAM standby
5. Juego en SSD, no en HDD de 5400 rpm
6. Resolución y preset realistas para tu hardware

## Preguntas frecuentes

**¿32 GB de RAM dan más FPS que 16 GB?** Solo si 16 GB se quedaban cortos. Si un juego usa 10 GB, pasar a 32 GB no magic boost.

**¿NVMe vs SATA para Fortnite?** Casi igual en FPS; NVMe gana en instalar y cargar lobby.

**¿Overclock de RAM merece la pena?** Rendimiento marginal; estabilidad y XMP/EXPO bien configurado suelen bastar.

**¿Optimus sube FPS?** No overclockea GPU. Reduce ruido del sistema, libera RAM y prepara el PC — útil en equipos justos de RAM o con mucho background.

**¿iGPU (sin tarjeta dedicada)?** La GPU integrada limita todo; la RAM compartida y la CPU pesan el doble. Para gaming serio hace falta gráfica dedicada.

## Conclusión

- **GPU** → calidad visual y FPS medios en la mayoría de AAA
- **CPU** → FPS mínimos y juegos exigentes en lógica
- **RAM** → fluidez cuando hay poca o el sistema va lleno
- **Disco** → cargas y streaming; rara vez el FPS en escena cerrada

Conoce tu cuello de botella, mejora con criterio y mantén Windows limpio. **Optimus** te ayuda en RAM, inicio, disco y modo gamer — gratis y local en Windows 10/11.
