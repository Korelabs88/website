## Por qué Windows se queda sin RAM

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
