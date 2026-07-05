Decidiste empezar a streamear. Investigaste, viste videos, leíste guías, y llegaste a una conclusión que te pareció lógica: necesitás la PC más potente posible, porque vas a tener que jugar Y grabar Y transmitir Y mostrar la cámara Y el chat, todo al mismo tiempo, en la misma máquina. Ahorraste durante meses, o directamente te endeudaste un poco, y compraste el monstruo: la CPU más rápida del mercado, la GPU tope de gama, toda la RAM que pudiste pagar.

Empezaste a streamear. Y ahí notaste algo raro: tus FPS en el juego caían de forma notoria apenas activabas la transmisión. El video que veían tus espectadores tenía micro-cortes ocasionales. Vos, jugando, sentías que el juego "se ponía pesado" justo quince minutos después de empezar el stream, como si la transmisión en sí misma le estuviera robando recursos al juego que se supone que era lo importante.

Mientras tanto, ves streamers con setups aparentemente mucho más modestos que el tuyo, con una PC de gama media y una segunda PC (o una capturadora dedicada) para manejar la transmisión, jugando con FPS perfectos, transmitiendo en calidad impecable, sin ningún tipo de sacrificio visible.

¿Cómo puede ser que tu PC "de streamer" carísima rinda peor que la combinación de dos máquinas más modestas? Bienvenido a una de las paradojas más caras (literalmente) de todo el ecosistema de contenido gamer moderno.

## Streaming no es "un poco más de trabajo": es otro trabajo entero, corriendo en paralelo

El error de fondo, el que lleva a comprar mal desde el principio, es pensar en streamear como una tarea liviana adicional que se le suma al juego, del estilo "bueno, ya que estoy jugando, transmito también, no debería ser tanto esfuerzo extra". La realidad técnica es completamente distinta: transmitir en vivo implica correr un proceso de codificación de video en tiempo real, comprimiendo cada frame que se genera, en simultáneo con el renderizado del propio juego. Es, en términos de carga de trabajo real para tu hardware, básicamente correr dos programas exigentes al mismo tiempo, compitiendo por los mismos recursos limitados de una sola máquina.

Esto significa que cuando streameás desde una sola PC, tu CPU y tu GPU no están dedicadas exclusivamente a darte los mejores FPS posibles en el juego. Están divididas: una parte de esos recursos, que puede ser bastante significativa según la configuración de codificación que uses, se la está llevando el proceso de comprimir y enviar tu transmisión en vivo, en paralelo a todo lo demás.

| Tarea en single-PC stream | Quién compite por recursos |
|---------------------------|----------------------------|
| **Renderizado del juego** | GPU + CPU |
| **Codificación OBS (x264)** | CPU (duro con el juego) |
| **NVENC / AMF / QuickSync** | Chip dedicado, pero VRAM/ancho de banda compartido |
| **Navegador, chat, alertas** | RAM + CPU en segundo plano |
| **Webcam + overlays** | Más GPU/CPU |

## Por qué comprar "más potencia" no resuelve el problema de raíz

Acá está el error de razonamiento que lleva a gastar mal: pensar que el problema de rendimiento al streamear se soluciona simplemente con "más hardware potente en general". Y aunque parcialmente ayuda (una CPU más rápida sí puede manejar mejor la codificación de software, por ejemplo), no ataca la raíz del problema, que es estructural: **estás pidiéndole a una sola máquina que haga simultáneamente dos tareas que compiten directamente por los mismos recursos limitados**, sin importar cuán grande sea el balde de recursos disponible.

Es parecido a comprar un auto cada vez más grande pensando que así vas a poder llevar más gente cómodamente, cuando el problema real es que estás tratando de manejar el auto y, al mismo tiempo, coordinar la logística completa de un evento desde el asiento del conductor mientras vas a alta velocidad. No importa cuán grande sea el auto: seguís tratando de hacer dos trabajos serios en simultáneo, con una sola persona (o, en este caso, un solo conjunto de recursos) manejando todo.

Conecta directo con la paradoja de **compraste la GPU equivocada**: más potencia en un solo componente no arregla un problema de **arquitectura** — acá, una sola máquina haciendo dos trabajos.

## La solución estructural: separar las dos tareas en dos sistemas distintos

Acá es donde entra la lógica del setup de dos PCs (o su alternativa más accesible, la capturadora dedicada), que resuelve el problema no con más potencia bruta en un solo lugar, sino con una división de trabajo mucho más inteligente:

**PC de juego**: se dedica exclusivamente a correr el juego, sin ninguna carga adicional de codificación de video para streaming. Toda su CPU y GPU están disponibles al 100% para maximizar tus FPS y minimizar el input lag, exactamente como si no estuvieras transmitiendo nada.

**PC de captura/streaming (o capturadora dedicada)**: recibe la señal de video de la PC de juego mediante un cable de captura, y se encarga exclusivamente de codificar y enviar esa señal a la plataforma de streaming, sin competir jamás por los recursos que necesita el juego para correr bien.

| Setup | Costo típico | Juego | Stream |
|-------|--------------|-------|--------|
| **1 PC tope + NVENC** | Alto | Bueno, con compromisos | Bueno |
| **PC juego media + capturadora** | Medio | Excelente | Muy bueno |
| **2 PCs modestas** | Medio-bajo | Excelente | Excelente |
| **1 PC tope sin separar tareas** | Muy alto | A veces peor que media+2ª | Variable |

Con este esquema, ninguna de las dos tareas le roba recursos a la otra, porque literalmente están corriendo en hardware físicamente separado. El resultado: podés tener una PC de gama media perfectamente capaz de correr tu juego a FPS altísimos y estables, combinada con una segunda máquina modesta (o incluso una capturadora externa relativamente económica) dedicada pura y exclusivamente a manejar la transmisión, sin sacrificar absolutamente nada en ninguno de los dos frentes.

## "Pero las capturadoras y GPUs modernas tienen codificación por hardware, ¿no alcanza con eso?"

Es una pregunta válida y merece una respuesta honesta, porque la tecnología avanzó bastante en este sentido. Las GPUs modernas, tanto de Nvidia como de AMD e Intel, incluyen motores de codificación de video dedicados (NVENC en el caso de Nvidia, por ejemplo) que permiten codificar la señal de streaming usando un chip separado de los núcleos principales que corren el juego, reduciendo muchísimo el impacto directo sobre tus FPS comparado con la codificación por software tradicional (que sí usa directamente la CPU principal, compitiendo de lleno con el juego).

Esto hizo que streamear desde una sola PC con una GPU moderna sea muchísimo más viable de lo que era hace algunos años, y para la mayoría de los streamers casuales o de audiencia chica/mediana, es una solución perfectamente razonable que no amerita necesariamente el gasto y la complejidad de un setup de dos máquinas.

Pero incluso con codificación por hardware dedicada, sigue existiendo cierto costo compartido: memoria de video (VRAM) usada simultáneamente por el juego y por el proceso de codificación, ancho de banda de memoria compartido, y en configuraciones de streaming más exigentes (mayor resolución, mayor bitrate, mayor calidad de codificación), ese costo compartido empieza a notarse más, especialmente en juegos que ya de por sí exigen mucho de esa misma GPU para el renderizado.

Es decir: la codificación por hardware suavizó muchísimo esta paradoja, pero no la eliminó por completo, sobre todo para quienes buscan la máxima calidad de transmisión posible sin ningún compromiso en el juego.

También conecta con **RAM standby** y **PC limpio con 8 apps**: OBS + navegador + Discord + alertas comen margen que el juego necesita en picos — ahí **Optimus** puede ayudar en single-PC antes de comprar otra GPU.

## Entonces, ¿para quién tiene sentido cada opción?

**Una sola PC con codificación por hardware moderna**: tiene sentido para streamers casuales, de audiencia chica o mediana, que no necesitan la máxima calidad de transmisión posible y que priorizan simplicidad de setup y menor costo total. Para la gran mayoría de la gente que empieza en streaming, esta es la opción más razonable para arrancar.

**Setup de dos PCs o capturadora dedicada**: tiene sentido para streamers que ya tienen una audiencia consolidada que exige alta calidad de transmisión constante, para quienes juegan títulos muy exigentes gráficamente donde cualquier recurso compartido se nota, o para quienes simplemente quieren la garantía absoluta de que su rendimiento en el juego nunca se va a ver afectado por el hecho de estar transmitiendo, sin importar cuán exigente sea la configuración de streaming elegida.

## El verdadero error: gastar en la dirección equivocada del problema

Esta paradoja conecta directamente con la primera de toda la serie: el error de comprar el componente equivocado pensando que "más potente en general" resuelve automáticamente cualquier problema de rendimiento. Acá pasa exactamente lo mismo, pero a nivel de arquitectura completa del setup: comprar una sola PC brutalmente potente pensando que así vas a poder jugar y transmitir sin compromisos es, muchas veces, gastar mucho más dinero del necesario en un lugar que no resuelve el problema estructural de raíz, cuando invertir esa misma plata (o incluso menos) en separar las tareas en dos sistemas distintos puede darte un resultado final muchísimo mejor en ambos frentes.

No se trata de tener el hardware más caro. Se trata de entender qué problema estás tratando de resolver realmente, y elegir la arquitectura de solución correcta para ese problema específico, en vez de asumir que "más potencia en un solo lugar" siempre es la respuesta.

## Preguntas frecuentes

**¿Capturadora Elgato HD60 vale vs segunda PC?** Para muchos, sí: separa codificación sin armar PC completa. Segunda PC da más flexibilidad (escenas, filtros, multistream).

**¿x264 Slow en CPU tope?** Compite directo con juegos CPU-bound. NVENC/AV1 en GPU moderna suele ser mejor trade-off en single-PC.

**¿144Hz + stream single-PC?** Si el 1% low cae al activar OBS, el monitor no importa — ver paradoja **300 FPS y se siente mal**.

**¿Empezar con qué?** Single-PC + NVENC + bitrate razonable. Segunda máquina o capturadora cuando el cuello de botella sea estructural, no "falta de RTX".

## La lección real

Streamear no es una tarea liviana que se le suma gratis a jugar: es, en términos de carga real para tu hardware, prácticamente un segundo trabajo corriendo en paralelo. Pretender resolver esa carga doble con una sola máquina, por más potente que sea, es pedirle a un solo sistema que haga bien dos trabajos que compiten estructuralmente por los mismos recursos.

Dos máquinas modestas, cada una dedicada a una sola tarea, casi siempre le van a ganar en resultado final a una sola máquina carísima tratando de hacerlo todo a la vez. No porque la máquina cara sea mala. Sino porque le estás pidiendo que resuelva con fuerza bruta un problema que en realidad se resuelve con división de trabajo.

Más paradojas en el **índice de paradojas del gaming** (enlace al final de esta página).
