Vas a la tienda, o entrás a la web, y ahí está: el NVMe Gen5, la bestia de las velocidades de transferencia, con números en la caja que parecen sacados de un servidor de datacenter. 12.000, 14.000 megabytes por segundo. Comparado con tu viejo SSD SATA, que corre a unos modestos 550 MB/s, parece que estuvieras comparando un cohete con un triciclo.

Lo comprás. Lo instalás. Reinstalás tu juego favorito. Y notás... que carga un poco más rápido al entrar al mapa. Nada más.

En combate, disparando, moviéndote, reaccionando a lo que pasa en pantalla: exactamente los mismos FPS que tenías antes. La misma sensación. El mismo juego. Pagaste una fortuna por una velocidad que sentís durante literalmente los quince segundos que tarda una pantalla de carga, y ni un segundo más.

Bienvenido a una de las compras más incomprendidas del mundo gamer: el disco no es tu cuello de botella de FPS, y probablemente nunca lo fue.

## Para qué sirve realmente un SSD (y para qué no)

El disco de tu PC tiene un trabajo muy claro y muy limitado dentro del ecosistema de rendimiento: **mover datos entre el almacenamiento permanente y la memoria RAM/VRAM cuando el juego los necesita**. Eso es todo. No calcula física, no dibuja frames, no procesa inteligencia artificial de enemigos. Solo transporta información de un lado a otro.

Esto significa que el disco importa muchísimo en momentos muy específicos:

- **Al iniciar el juego** (cargar todos los assets básicos por primera vez).
- **Al cargar un nivel o mapa nuevo** (streaming de texturas, modelos, sonidos).
- **Al hacer un viaje rápido o teletransportarte** en un mundo abierto.
- **En streaming de mundo abierto en tiempo real**, cuando el juego va cargando terreno nuevo mientras te movés a gran velocidad (por ejemplo, en un juego de mundo abierto con vehículos rápidos).

Pero una vez que el nivel ya está cargado en RAM y VRAM, el disco prácticamente deja de participar en el proceso. Durante el combate, disparando, esquivando, reaccionando, el trabajo pesado lo hacen la CPU (lógica, física, IA) y la GPU (dibujado de cada frame). El disco, en ese momento, está tranquilamente sentado sin hacer nada, esperando la próxima vez que lo necesiten.

Por eso, comparar un NVMe Gen5 carísimo contra un SATA modesto casi nunca muestra diferencia en FPS durante el gameplay real: **ninguno de los dos está trabajando en ese instante**.

| Momento | ¿El disco trabaja? | ¿Afecta FPS? |
|---------|-------------------|--------------|
| Pantalla de carga / lobby | **Sí, mucho** | No (aún no jugás) |
| Combate estable en nivel cargado | **Casi no** | **No** |
| Mundo abierto a alta velocidad | **Sí, streaming** | A veces (pop-in, no FPS teórico) |
| Explosión con muchos efectos | **No** | No — CPU/GPU |

## El benchmark que nadie te muestra (pero que deberías pedir)

Las reviews de hardware, sobre todo las patrocinadas o las que buscan views fáciles, adoran mostrarte gráficos de "tiempos de carga": SSD A carga el nivel en 4 segundos, SSD B lo carga en 9 segundos. Se ve una diferencia enorme en el gráfico de barras, genera un titular llamativo, y empuja ventas.

Lo que casi nunca te muestran, porque es mucho menos vistoso, es un gráfico comparando los FPS durante el combate real usando cada uno de esos discos. Y la razón por la que no te lo muestran es simple: **esa gráfica sería una línea prácticamente plana e idéntica entre ambos discos**, porque no hay nada interesante que mostrar ahí. El disco ya cumplió su función al principio del nivel.

Es un poco como comparar dos ascensores por lo rápido que suben al piso 20, y después medir la velocidad a la que caminás dentro de tu oficina una vez que ya llegaste. Un ascensor puede ser el doble de rápido que el otro. Pero adentro de la oficina, caminando, la velocidad del ascensor ya no tiene absolutamente nada que ver con nada.

## "Pero en juegos de mundo abierto sí se nota, ¿no?"

Acá hay que ser honestos y no caer en el extremo contrario de decir "el SSD no sirve para nada", porque eso sería igual de falso. En juegos de mundo abierto moderno, con streaming agresivo de texturas mientras te movés rápido (pensá en un juego con autos a alta velocidad, o un shooter de extracción con mapas gigantes), un disco lento puede generar un problema muy real y muy visible: **pop-in**, es decir, texturas que aparecen borrosas y se van definiendo de a poco frente a tus ojos, o directamente objetos que tardan en aparecer.

En estos casos específicos, pasar de un disco mecánico viejo (HDD) a un SSD SATA es una mejora bestial, notoria, innegable. El salto de "nada carga bien" a "todo carga bien" es enorme.

Pero acá está la parte importante de la paradoja: **el salto de un SSD SATA decente a un NVMe Gen5 tope de gama, en la inmensa mayoría de los juegos actuales, es marginal**. La diferencia entre "andar bien" y "andar espectacularmente bien en la carga" no se traduce en una diferencia proporcional en tu experiencia real jugando. El salto grande de mejora ya lo diste antes, cuando dejaste el disco mecánico. Lo que viene después es una carrera de rendimientos decrecientes, donde pagás muchísimo más por una mejora cada vez más chica y cada vez menos perceptible.

| Upgrade de disco | Impacto en cargas | Impacto en FPS en combate |
|------------------|-------------------|---------------------------|
| **HDD → SATA SSD** | Enorme | Casi ninguno* |
| **SATA SSD → NVMe Gen3/4** | Notable | Casi ninguno |
| **NVMe Gen4 → Gen5** | Pequeño | Casi ninguno |

\*En HDD algunos open world **sí** stutterean por no leer texturas a tiempo — no es menos FPS en el contador, son **hitches** al girar.

## El verdadero problema: gastaste en el lugar equivocado del sistema

Esta paradoja del SSD conecta directamente con la primera paradoja que vimos sobre el **bottleneck de CPU y GPU**: el rendimiento real de tus FPS en combate depende del componente que está trabajando en ese instante, no del que gastaste más plata en la caja. El disco casi nunca es ese componente durante el gameplay activo. Es CPU y GPU, casi siempre, con la RAM jugando un rol de soporte importante también.

Entonces, cuando alguien con un presupuesto limitado me pregunta "¿me conviene el NVMe Gen5 carísimo o me sirve más meter esa plata en otro lado?", la respuesta casi siempre es la misma: esa plata rinde muchísimo más invertida en GPU, en CPU, o incluso en más RAM, que en la última generación de velocidad de disco. El disco es el componente con menor impacto directo en tus FPS de todo el sistema, siempre que ya hayas superado la barrera básica de tener un SSD (cualquier SSD razonable) en vez de un disco mecánico.

Orden típico de impacto en **FPS y fluidez en combate**:

1. **GPU** (resolución, calidad gráfica)
2. **CPU** (1080p competitivo, multitudes, física)
3. **RAM** (margen para picos — ver paradoja de la RAM "llena")
4. **Disco** (cargas y streaming; rara vez FPS en escena cerrada)

Para el desglose completo, consultá la guía sobre **RAM, GPU, CPU y disco en juegos** (enlace al final).

## ¿Entonces cuándo SÍ vale la pena un NVMe de última generación?

No es que estos discos sean malos productos, ojo. Tienen sentido en escenarios muy puntuales:

**1. Trabajo profesional con archivos enormes.**

Edición de video en 4K/8K, manipulación de archivos masivos, transferencias constantes de datos pesados. Ahí la velocidad bruta sí se traduce en tiempo real ahorrado, todos los días.

**2. Tiempos de carga en juegos con niveles gigantes y frecuentes recargas.**

Si jugás algo con muchísimos loading screens (por ejemplo, un juego competitivo donde reiniciás rondas constantemente), ahorrarte unos segundos por carga, multiplicado por cientos de veces al día, sí puede sumar una comodidad real, aunque no afecte tus FPS.

**3. Espacio y organización, más que velocidad.**

A veces la razón real para upgradear el disco no es velocidad, es simplemente tener más espacio para instalar más juegos sin tener que estar desinstalando todo el tiempo.

**4. DirectStorage y juegos que lo explotan.**

Algunos títulos en PC usan carga directa desde NVMe a la GPU. Todavía es nicho, pero ahí la velocidad del disco puede importar más que en el juego promedio.

Si tu motivación real es alguna de estas, la compra tiene sentido. Si tu motivación es "quiero más FPS en combate", ese dinero está mejor invertido en otra parte de tu setup — empezando por diagnosticar si tu límite es CPU o GPU, no el disco.

### Lo mínimo que sí deberías tener (sin gastar de más)

- Juegos en **SSD**, no en HDD de 5400 rpm
- **20 %+ libre** en el disco del sistema (Windows y shaders cachean ahí)
- Limpieza ocasional de temporales (**Optimus** incluye limpieza reversible de disco)
- No confundir "carga más rápida" con "juego más fluido en ranked"

## Preguntas frecuentes

**¿NVMe Gen5 sube FPS en Warzone / Valorant?** Casi nunca en partida. Puede acortar lobby y reinicios de ronda.

**¿Merece la pena pasar juegos de SATA a NVMe?** Si ya tenés SATA, el salto en FPS en combate suele ser cero. En cargas, a veces unos segundos menos — comodidad, no skill.

**¿El disco lento causa stuttering?** Sí en **HDD** y open world con streaming agresivo. En SSD vs SSD top, rara vez.

**¿Dónde instalo el SO y los juegos?** SO en SSD rápido; juegos que más jugás en el mismo SSD. No hace falta Gen5 para el 95 % de títulos.

**¿Presupuesto limitado: SSD grande o GPU mejor?** GPU (o CPU si estás limitado en 1080p). Un SATA SSD de 1 TB + GPU un escalón arriba casi siempre gana para FPS.

## La lección real

El disco es el componente más malentendido de todo el armado de una PC gamer, porque su beneficio es real, pero está encapsulado en un momento muy específico y acotado de tu sesión de juego: la carga inicial. Una vez que el nivel ya está en memoria, el disco se convierte en un espectador silencioso del resto de tu partida.

Pagar una fortuna por el disco más rápido del mundo pensando que eso va a mejorar tu rendimiento en combate es como comprar el auto más rápido del mundo para el trayecto de tu casa al garage. Vas a llegar rapidísimo al garage. Una vez adentro, estacionado, la velocidad máxima del auto deja de importar completamente.

Gastá en lo que trabaja mientras jugás, no solo en lo que trabaja antes de que empieces a jugar.
