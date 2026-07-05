Te pasó, o le pasó a algún amigo tuyo, seguro. Actualizás tu setup, activás el contador de FPS en la esquina de la pantalla, y ahí está: 280, 300, a veces picos de 340. Un número que hace unos años solo veías en configuraciones de laboratorio para benchmarks. Deberías estar viviendo la experiencia gamer más fluida de tu vida.

Y sin embargo, algo anda mal. El juego se siente entrecortado. Hay microtirones que aparecen de la nada, sobre todo en los momentos más intensos: una explosión grande, un giro brusco de cámara, el momento exacto en que tenés que reaccionar rápido para no morir. Mirás el contador, dice 290 FPS, y pensás: "¿cómo puede sentirse mal esto si el número es altísimo?".

Bienvenido a una de las mentiras más grandes que nos vendió la cultura del benchmark: que el FPS promedio es sinónimo de fluidez. No lo es. Y entender por qué te va a cambiar completamente la forma en que evaluás el rendimiento de tu PC.

## El promedio es un maquillaje estadístico

Pensá en el FPS promedio como el promedio de sueldos de una empresa. Si en una oficina de diez personas, nueve ganan un sueldo normal y una sola (el dueño) gana una fortuna, el "promedio" de la oficina va a dar un número bastante alto y engañoso. Ese promedio no representa la realidad de la mayoría de la gente que trabaja ahí.

El FPS promedio funciona exactamente igual. Si tu juego corre a 400 FPS en los momentos tranquilos (mirando una pared, parado en el spawn) y cae a 60 FPS en los momentos de acción real (combate, muchos efectos en pantalla, explosiones), el promedio final puede seguir marcando un número altísimo, tipo 290 FPS, aunque la experiencia real, en el momento que más te importa (justo cuando estás jugando de verdad, no mirando una pared), sea mucho peor de lo que ese número sugiere.

El promedio te miente porque mezcla lo fácil de renderizar con lo difícil, y deja que lo fácil "tape" lo difícil.

| Métrica | Qué mide | ¿Refleja la fluidez real? |
|---------|----------|---------------------------|
| **FPS promedio** | Media de toda la sesión | **No** — oculta los valles |
| **1 % low** | Peor 1 % de frames | **Sí** — tus peores momentos |
| **0,1 % low** | Peor 0,1 % de frames | **Sí** — microcortes extremos |
| **Frame time (ms)** | Milisegundos por frame | **Sí** — lo que sentís al mover la cámara |

## Acá entra el verdadero héroe de esta historia: el 1% low

El **1% low** (y su primo un poco más estricto, el **0,1% low**) es una métrica que no mide el promedio general, sino específicamente **el rendimiento en el peor 1% de los frames que generaste**. En otras palabras: en vez de preguntarte "¿cómo rendiste en general?", te pregunta "¿qué tan mal la pasaste en tus peores momentos?".

Esta métrica es muchísimo más honesta sobre cómo se *siente* jugar, porque tu cerebro no percibe el promedio de una sesión. Tu cerebro percibe los picos y los valles. Un tirón de medio segundo en el momento exacto en que ibas a reaccionar a un enemigo es lo que te cuesta la partida, no el hecho de que dos segundos antes estuvieras corriendo a 350 FPS mirando el cielo.

Un ejemplo concreto: dos PCs, mismo juego.

**PC A**: FPS promedio de 240. 1% low de 55.

**PC B**: FPS promedio de 165. 1% low de 130.

En el papel, la PC A "gana" por un margen enorme si solo mirás el promedio. Pero jugando, la PC B se va a sentir dramáticamente más consistente, más predecible, más "suave" en los momentos críticos. La PC A tiene picos espectaculares seguidos de bajones bruscos que se sienten como tropezones. La PC B mantiene un piso mucho más estable, aunque su techo sea más bajo.

Casi cualquier jugador competitivo, si probara ambas configuraciones a ciegas sin ver el número en pantalla, elegiría la sensación de la PC B como "más fluida", aunque su número promedio sea más chico.

## ¿Por qué pasan estos bajones si el hardware es potente?

Acá hay varias causas típicas, y vale la pena conocerlas porque cada una tiene una solución distinta:

**1. Stutters de compilación de shaders.**

Muchos juegos modernos compilan efectos gráficos (shaders) la primera vez que los ven en pantalla, no antes. Esto genera microtirones específicamente cuando aparece un efecto nuevo (una explosión con un tipo de partícula que no habías visto todavía en esa sesión), sin importar lo potente que sea tu hardware. Algunos juegos precompilan shaders al iniciar para evitar esto; otros, lamentablemente, no.

**2. Falta de margen de RAM o VRAM en momentos de pico.**

Como vimos en la nota sobre **tu RAM no está "llena", está trabajando**, cuando el sistema necesita reorganizar memoria de golpe (por ejemplo, al cargar muchos efectos nuevos en una explosión grande), ese reacomodo genera una pausa perceptible, aunque tu promedio general de FPS sea altísimo.

**3. Procesos en segundo plano que despiertan en el peor momento.**

Un antivirus haciendo un escaneo programado, Windows Update bajando algo en segundo plano, Discord procesando una notificación con imagen: todo esto puede generar micro-competencia por recursos justo en el momento más intenso del juego, sin afectar demasiado tu promedio general (porque son eventos cortos), pero destrozando tu 1% low.

**4. Limitaciones de CPU en escenas con mucha lógica simultánea.**

Una explosión grande no es solo un efecto visual: implica calcular físicas, múltiples hitboxes, sonido posicional, IA reaccionando. Toda esa carga de golpe puede generar una caída puntual de frames aunque el resto del tiempo tu CPU esté sobrando.

| Causa del bajón | Síntoma típico | Qué probar |
|-----------------|----------------|------------|
| Shaders sin compilar | Tirón la primera vez que ves un efecto | Precompilar shaders / jugar una ronda de calentamiento |
| RAM/VRAM justa | Stutter en combate + disco activo | Cerrar apps, liberar standby, más RAM/VRAM |
| Background | Tirones aleatorios, no ligados al juego | Modo gamer, cerrar overlays, posponer updates |
| CPU limit | GPU con margen, 1% low bajo en multitudes | Mejor CPU o bajar settings que cargan lógica |

## El error de "optimizar para el número"

Acá está el corazón de la paradoja, y por eso el título de esta nota no es casualidad. Mucha gente, al buscar mejorar su experiencia, se obsesiona con subir el promedio: baja configuraciones gráficas, activa mods de rendimiento, todo con el objetivo de ver un número más alto en la esquina de la pantalla. Y a veces lo logran: el promedio sube de 220 a 280.

Pero si esas mismas configuraciones no atacan la causa real de los bajones puntuales (shaders sin precompilar, memoria sin margen, procesos de fondo compitiendo por recursos), el 1% low sigue igual de mal, o incluso empeora, porque ahora hay más frames "fáciles" tapando estadísticamente los mismos frames "difíciles" de siempre.

Es como intentar mejorar el tiempo promedio de un corredor haciéndolo correr más rápido en los tramos llanos, sin arreglar el hecho de que se cae en cada pozo del camino. El promedio general de velocidad puede mejorar en el papel. La experiencia de correr esa pista, con esos pozos intactos, sigue siendo igual de mala.

Relacionado: activar DLSS para subir el promedio sin mejorar los lows es la misma trampa al revés — a veces el upscaling **sí** mejora ambos; a veces solo infla el número en escenas fáciles. Más en nuestra guía sobre **DLSS y FSR vs resolución nativa** (enlace al final).

## Entonces, ¿qué número deberías mirar en vez del promedio?

Si tu objetivo es una experiencia que realmente se sienta fluida y no solo que "mida bien" en una captura de pantalla con el contador de FPS, priorizá:

**1. El 1% low como referencia principal**, no el promedio. Herramientas como MSI Afterburner, CapFrameX o el overlay de muchos juegos ya te muestran esta métrica directamente.

**2. La consistencia del frame time**, más que el número puro. Un gráfico de frame time con una línea relativamente plana es más valioso que uno con picos altísimos y valles profundos, aunque el promedio de ambos sea idéntico.

**3. Cómo se siente en los momentos de mayor exigencia real del juego**, no en el menú principal o parado en el spawn. Andá directo a la zona más caótica de combate o a la escena con más efectos, y evaluá ahí, no en la calma.

### Checklist rápido antes de culpar al hardware

1. Medí **1% low** en combate real, no en menú
2. Precompilá shaders si el juego lo permite
3. Cerrá background pesado; **modo gamer de Optimus** antes de ranked
4. Verificá RAM y VRAM en el pico (Administrador de tareas / Afterburner)
5. Drivers GPU al día

Para entender qué componente limita tu PC (CPU, GPU, RAM, disco), consultá la guía sobre **RAM, GPU, CPU y disco en juegos** (enlace al final).

## Preguntas frecuentes

**¿Cuánto 1% low es "bueno"?** Depende del juego y refresh del monitor. Regla práctica: que el 1% low no caiga por debajo de ~80 % de tu refresh (ej.: en 144 Hz, idealmente lows >115 FPS). En 60 Hz, lows estables >50 FPS ya se sienten bien.

**¿Cap a 141 FPS ayuda la fluidez?** A veces sí: limitar FPS puede estabilizar frame pacing en algunos títulos. Probá con V-Sync off + cap en Afterburner.

**¿Más FPS siempre = menos input lag?** En general sí hasta cierto punto, pero si los lows son basura, el input se siente inconsistente aunque el promedio sea alto.

**¿Optimus sube el 1% low?** No overclockea. Libera RAM y reduce ruido de fondo — útil si tus lows vienen de memoria o procesos compitiendo, no de GPU pura.

**¿Frame Generation (DLSS 3) mejora lows?** Sube FPS perceptibles pero puede añadir latencia; en competitivo priorizá lows reales sin generación de frames.

## La lección real

Un número grande en la esquina de la pantalla es adictivo, es fácil de comparar con tus amigos, y es fácil de vender en el marketing de una GPU nueva. Pero no es lo que tu cerebro realmente percibe como "jugar bien". Tu cerebro percibe consistencia. Percibe que cuando gira la cámara, la imagen responde sin sorpresas. Percibe que en el momento exacto de la explosión, el juego no te traiciona con medio segundo de pausa justo cuando querés reaccionar más rápido que nunca.

La próxima vez que evalúes si tu PC "anda bien" o si necesitás un upgrade, dejá de mirar solo el promedio. Fijate en tus peores momentos, no en tus mejores. Porque en los juegos, como en la vida, uno no recuerda el promedio de una noche. Recuerda el instante exacto en que algo salió mal.

Y ese instante no lo mide el FPS promedio. Lo mide el 1% low.
