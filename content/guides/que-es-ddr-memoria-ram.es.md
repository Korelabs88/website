## Qué es DDR (Double Data Rate)

**DDR** significa *Double Data Rate*: la memoria transfiere datos **dos veces por ciclo de reloj** (en el flanco de subida y en el de bajada). Por eso, si ves "3200 MHz" en un módulo DDR4, la frecuencia real del bus es 1600 MHz, pero el dato efectivo es el doble.

Es la memoria **RAM** que usa tu PC de escritorio o portátil: la que Windows muestra en Configuración → Sistema → Memoria y en el Administrador de tareas. No confundirla con la VRAM de la gráfica ni con el almacenamiento SSD.

### Para qué sirve en la práctica

- Mantener abiertos programas, pestañas y archivos en uso
- Cachear datos que el procesador necesita al instante
- Reducir accesos al disco (mucho más lento que la RAM)

Cuanto más RAM tengas y más rápida sea, menos dependerás del disco y menos "atascos" notarás al multitarea o al jugar.

## ¿Por qué hay 5 generaciones?

En realidad hablamos de **cinco estándares sucesivos** comercializados para PCs:

| Generación | Época aproximada | Característica clave |
|------------|------------------|----------------------|
| **DDR** (DDR1) | 2000–2005 | Primera DDR de consumo; reemplazó SDRAM |
| **DDR2** | 2005–2010 | Menor voltaje, más densidad |
| **DDR3** | 2010–2015 | Aún menos consumo; hasta 2133 MHz efectivos |
| **DDR4** | 2015–2021 | Gran salto de ancho de banda; estándar durante años |
| **DDR5** | 2021–actualidad | Doble canal por módulo, mayor capacidad por DIMM |

No conviven entre sí: **cada generación usa ranura, voltaje y señales distintas**. No puedes insertar un DDR4 en una placa solo DDR5. Por eso, al ampliar RAM, debes comprar exactamente lo que soporta tu placa base y tu procesador.

### ¿Por qué no se quedaron en una sola?

Cada salto responde a necesidades reales del mercado:

1. **Más ancho de banda** para CPUs y GPUs cada vez más rápidas
2. **Menor consumo** (importante en portátiles y servidores)
3. **Módulos de mayor capacidad** (32 GB, 48 GB, 64 GB por palito en DDR5)
4. **Nuevas funciones** (en DDR5: PMIC en el módulo, dos canales independientes por DIMM)

Cuando una generación deja de cubrir el rendimiento de los procesadores nuevos, JEDEC (el consorcio que define estándares) publica la siguiente.

## DDR5 hoy: qué aporta frente a DDR4

- Velocidades de serie desde 4800 MT/s hacia arriba (frente a 2133–3200 típicos en DDR4)
- Mejor eficiencia energética por bit transferido
- Capacidades mayores por módulo sin depender de chips raros
- Ideal para gaming moderno, edición de video y cargas con mucha RAM en standby

Si tu PC aún usa DDR4, **no es obligatorio saltar**: sigue siendo válido. El cambio tiene sentido al montar un equipo nuevo o al actualizar placa + CPU.

## ¿Cuándo llegará el DDR6?

A **julio de 2026** no hay un estándar DDR6 publicado ni módulos de consumo en tienda. Lo que sí existe es trabajo previo de la industria:

- **JEDEC** y fabricantes (Samsung, SK Hynix, Micron) han hablado de desarrollo activo
- Estimaciones públicas apuntan a **definición del estándar hacia 2026–2027** y productos masivos **varios años después** (como ocurrió con DDR5, anunciado en 2018–2020 y generalizado en PCs hacia 2022–2024)

En resumen: **DDR6 no está a la vuelta de la esquina para tu próximo PC de hoy**, pero es el siguiente paso lógico en la hoja de ruta.

### Señales realistas de calendario

| Fase | Cuándo (estimación) |
|------|---------------------|
| Borrador / especificación JEDEC | 2026–2027 |
| Primeros módulos enterprise / servidor | ~2027–2028 |
| Placas de consumo y precios razonables | 2028–2030 o más |

Las fechas exactas cambian según la economía, la demanda de IA en servidores y la madurez de las fábricas.

## Posibles ventajas del DDR6 frente al DDR5

Hasta que JEDEC publique el estándar final, parte de esto es **expectativa basada en tendencias**, no en specs cerradas. Aun así, esto es lo que la industria suele perseguir generación tras generación:

### 1. Más ancho de banda

Los CPUs y las cargas de IA piden cada vez más datos por segundo. DDR6 probablemente suba de nuevo los **MT/s** efectivos (transferencias por segundo), aliviando cuellos de botella en sistemas con muchos núcleos.

### 2. Menor consumo por bit

Mejoras en voltaje y en la lógica del módulo (como evolucionó el PMIC en DDR5) suelen repetirse: **misma velocidad con menos vatio**, o más velocidad con consumo similar.

### 3. Mayor densidad y capacidades

Esperable ver módulos **más gruesos en GB** sin multiplicar ranuras: útil para estaciones de trabajo, servidores y PCs que hoy ya piden 64–128 GB.

### 4. Fiabilidad y corrección de errores

En entornos profesionales, DDR6 podría reforzar **ECC on-die** o mecanismos similares ya esbozados en generaciones recientes, reduciendo errores silenciosos en cargas 24/7.

### 5. Preparación para nuevos buses

A medio plazo, la memoria debe alinearse con **placas base y CPUs** de Intel y AMD futuros. DDR6 será el companion lógico de procesadores que hoy aún no existen en tu tienda local.

**Importante:** tener DDR6 no sustituye tener **suficiente RAM instalada** ni un Windows bien gestionado. Un PC con 16 GB de DDR5 bien administrado puede ir más fluido que uno con 32 GB llenos de procesos en segundo plano.

## Qué puedes hacer hoy con tu RAM actual

Independientemente de si tienes DDR3, DDR4 o DDR5:

1. Comprueba cuánta RAM usa Windows en reposo (Configuración o **Optimus** en vivo)
2. Identifica procesos que comen memoria sin aportar valor
3. Si el PC va justo, valora **ampliar con la misma generación** antes que cambiar toda la plataforma
4. Libera memoria **standby** de forma segura cuando vayas a jugar o renderizar

**Optimus** monitoriza RAM, CPU y disco en tiempo real y puede purgar listas standby con operaciones nativas de Windows — gratis y sin subir datos a la nube.

## Preguntas frecuentes

**¿DDR y SDRAM es lo mismo?** No. SDRAM era la generación anterior; DDR fue la evolución "doble tasa" que domina desde 2000.

**¿Puedo mezclar marcas de RAM?** Sí, si comparten generación, voltaje y frecuencia compatible. Mejor pares idénticos para dual channel simétrico.

**¿Más MHz siempre es mejor?** Solo si la placa y el CPU lo soportan. Frecuencias fuera de spec pueden no arrancar o estabilizarse a valores menores.

**¿DDR6 hará obsoleto mi DDR5?** No de inmediato. Las transiciones tardan años; DDR4 sigue vendiéndose y usándose en 2026.

**¿Optimus acelera la RAM física?** No cambia tu hardware DDR. Optimiza **cómo Windows usa** la memoria que ya tienes: working sets, standby y caché del sistema.
