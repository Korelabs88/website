Son las 11 de la noche de un domingo. Mañana tenés que laburar o estudiar, pero eso no importa ahora, porque encontraste un video de YouTube de 45 minutos titulado "EL SETUP DEFINITIVO PARA +200 FPS - LOS PROS NO QUIEREN QUE SEPAS ESTO". Y ahí vas. Regedit abierto. Servicios de Windows deshabilitados uno por uno como si estuvieras desarmando una bomba. Un script de "debloat" que descargaste de un repositorio de GitHub con 4 estrellas y un README escrito medio en inglés medio en ruso. Un archivo .bat que prometía "liberar hasta un 40% más de rendimiento" y que corriste como administrador sin leer ni una línea de lo que hacía.

Tres horas después, con los ojos rojos y la autoestima de "genio de la optimización" a full, abrís tu juego para probar los frutos de tu trabajo.

Ganaste tres FPS.

O peor: perdiste estabilidad, y ahora el juego crashea cada cuarenta minutos porque desactivaste sin querer un servicio que en realidad sí hacía algo importante.

Bienvenido al deporte nacional del PC gaming: la sobreoptimización compulsiva. Vamos a hablar de por qué pasa esto, por qué es tan seductor, y sobre todo, por qué el PC más optimizado casi nunca es el más "tuneado".

## El encanto irresistible del tweak imposible de medir

Hay algo profundamente satisfactorio en desactivar un servicio de Windows que tiene un nombre que suena a villano de película de espías: "Superfetch", "Telemetría", "Cortana Background Process". Se siente como estás desmantelando una conspiración. Se siente productivo. Se siente a control.

El problema es que la mayoría de estos tweaks tienen un impacto real en el rendimiento de FPS que oscila entre "cero" y "estadísticamente indetectable sin un benchmark de laboratorio". Windows, en su configuración normal de fábrica, ya está bastante bien optimizado para la mayoría de las tareas, incluyendo jugar. La mayoría de los servicios que la gente desactiva con tanto orgullo ni siquiera están activos consumiendo recursos mientras jugás: están ahí, dormidos, esperando a que alguna vez los necesites (por ejemplo, para indexar archivos para que la búsqueda de Windows funcione mejor).

Desactivarlos no libera un ejército de recursos escondidos. Libera, en el mejor de los casos, una cantidad de RAM y CPU tan chica que ni el software de monitoreo más preciso la puede diferenciar del margen de error normal entre una partida y otra.

| Tweak típico de YouTube | Impacto real en FPS | Riesgo |
|-------------------------|---------------------|--------|
| Desactivar 20 servicios | ~0 | Medio (instabilidad) |
| "Debloat" masivo con script | ~0–3 | Alto (romper Windows) |
| Limpiar registro | ~0 | Alto (crashes) |
| Desactivar telemetría | ~0 | Bajo (pero no da FPS) |
| Drivers GPU al día | **+5–15 %** en juegos nuevos | Bajo |
| Cerrar Chrome + apps pesadas | **Notable** si RAM llena | Ninguno |

## El problema del "yo lo sentí más fluido"

Acá aparece el argumento más común de defensa de esta comunidad: "pero yo lo sentí más fluido después de aplicar los tweaks". Y mirá, no dudo de tu palabra. El problema es que el cerebro humano es una máquina espectacular de generar la sensación de mejora cuando *cree* que hizo algo para mejorar algo. Se llama efecto placebo, y no es exclusivo de la medicina: aplica igual de fuerte a configuraciones de PC.

Si pasaste tres horas de tu domingo tocando cosas, invirtiendo esfuerzo, sintiéndote un hacker de película, tu cerebro va a estar predispuesto a percibir cualquier mínima variación normal de rendimiento (que existe siempre, entre partida y partida, por mil factores random) como "la prueba" de que tu esfuerzo valió la pena. Es un sesgo de confirmación clásico, y es completamente humano. No te hace tonto. Te hace parte del 99% de las personas que alguna vez cayeron en esto.

La única forma real de saber si un tweak sirvió es benchmarking serio: mismo escenario del juego, misma configuración, múltiples corridas, antes y después, comparando números concretos de **FPS promedio y 1% low** — no solo la sensación. Casi nadie hace esto. Casi todos confían en la sensación subjetiva post-tweak, contaminada de entusiasmo y esfuerzo invertido.

Para entender por qué el promedio engaña, leé la nota sobre **300 FPS y se siente mal** (enlace al final).

## Cuando la sobreoptimización te sale por la culata

Acá está la parte donde el tema deja de ser gracioso y empieza a doler de verdad. Muchos de estos scripts de "debloat" y "optimización extrema" que circulan por internet no distinguen entre lo que es genuinamente prescindible y lo que en realidad Windows necesita para funcionar bien.

Casos reales y comunes:

- **Deshabilitar el Superfetch/SysMain** pensando que "libera RAM", cuando en realidad ese servicio es justamente el que gestiona la memoria standby inteligente que vimos en otra nota, la que hace que tus programas carguen más rápido. Al apagarlo, en vez de "liberar" nada, terminás con un sistema que tiene que cargar todo desde cero cada vez, más lento, no más rápido.
- **Desactivar servicios de Windows Update** de forma agresiva, generando que el sistema quede sin parches de seguridad y, en algunos casos, con incompatibilidades con drivers nuevos que sí afectan el rendimiento real.
- **Correr scripts de "limpieza de registro"** que terminan borrando entradas que sí eran necesarias, generando errores intermitentes, crasheos random, o hasta la necesidad de reinstalar Windows entero, después de lo cual el mismo usuario va a decir en un foro "che, mi PC anda re raro desde que optimicé todo".
- **Desactivar el Modo Núcleo Aislado o protecciones de seguridad de bajo nivel** pensando que "consumen recursos", cuando el impacto real en rendimiento es mínimo y el riesgo de seguridad que asumís es completamente desproporcionado a cambio de nada.

En el peor de los casos, terminás gastando más tiempo reparando lo que rompiste "optimizando" que el tiempo que ibas a ahorrarte jugando con esos 3 FPS extra que nunca llegaron.

## Entonces, ¿todo tweak de Windows es inútil?

No, y acá hay que ser justos. Existen ajustes genuinamente útiles, pero son mucho menos espectaculares y mucho menos "de hacker" de lo que el video de YouTube de turno te quiere vender. Cosas que sí tienen impacto real y medible:

**1. Actualizar drivers de GPU regularmente.**

Esto sí, consistentemente, trae mejoras de rendimiento reales, sobre todo en juegos nuevos donde el fabricante optimizó específicamente para ese título.

**2. Cerrar programas pesados innecesarios antes de jugar.**

No servicios ocultos del sistema operativo: programas reales que abriste vos y que están consumiendo CPU/RAM activamente (un navegador con veinte pestañas, un editor de video con un proyecto cargado).

**3. Modo de energía en "Rendimiento" en laptops.**

En equipos portátiles, esto sí puede generar una diferencia notable, porque el modo balanceado o ahorro de energía limita activamente la velocidad del procesador.

**4. Mantener el sistema con espacio libre razonable en el disco donde está instalado Windows.**

Un disco casi lleno sí puede generar problemas reales de rendimiento y estabilidad, esto no es mito.

**5. Usar herramientas pensadas específicamente para gestionar recursos antes de una sesión de juego**, en vez de scripts genéricos de dudosa procedencia. **Optimus** apunta justamente a esto: liberar lo que realmente compite por recursos en el momento de jugar (RAM standby, procesos de fondo), con **modo gamer**, sin tocar servicios internos del sistema que no tenés forma fácil de evaluar si son seguros de desactivar o no.

Para una guía con pasos concretos y seguros, ver **cómo optimizar Windows 11 para gaming** (enlace al final).

## Qué NO hacer (checklist anti-desastre)

- No corras scripts .bat de canales random como administrador
- No desactives servicios sin saber qué hacen
- No uses "registry cleaners" — Windows 11 no los necesita
- No desinstales Microsoft Store / Xbox services si jugás Game Pass
- No desactives SysMain creyendo que "libera RAM" — leé la paradoja de la **RAM standby**
- No confundas horas de tweaks con diagnóstico de **cuello de botella** real (CPU/GPU/RAM)

## Preguntas frecuentes

**¿Debloat de Chris Titus / scripts populares valen la pena?** Algunos pasos son razonables (desactivar animaciones). El paquete completo suele ser overkill y arriesgado para +0–3 FPS.

**¿Game Mode de Windows ayuda?** A veces sí, a veces no — depende del juego. No reemplaza cerrar apps pesadas.

**¿Desactivar telemetría da FPS?** Casi nunca. Privacidad sí; rendimiento no.

**¿Reinstalar Windows limpia el PC?** Sí, si tenés años de basura instalada. Pero es nuclear — probá drivers + cerrar background + Optimus antes.

**¿Cuánto FPS "real" puedo esperar de optimización software?** Si el hardware está bien: pocos FPS en promedio, a veces mejor **1% low** si RAM/background eran el problema. Si esperás +50 FPS, el límite es hardware o settings gráficos.

## La lección real (con toda la mala leche que se merece)

El PC más optimizado del mundo no es el que tiene el registro de Windows editado a mano como si fuera el código fuente de la Matrix. Es, la mayoría de las veces, un PC bastante normal, con drivers actualizados, sin programas pesados innecesarios corriendo de fondo, y con el usuario jugando en vez de perdiendo el domingo entero peleándose con servicios que ni sabía que existían hasta esa noche.

Así que la próxima vez que encuentres un video prometiendo "el secreto que las empresas no quieren que sepas" para ganar FPS gratis desactivando media docena de procesos misteriosos, hacete una pregunta simple: si esa optimización fuera real, medible, y sin riesgos... ¿no la habría implementado Windows por defecto hace rato, en vez de dejártela como secreto oculto en un canal de YouTube con miniatura de flechita roja y cara de sorpresa?

Guardate esas tres horas de domingo. Usalas para jugar. Es, con diferencia, la optimización más efectiva que existe.
