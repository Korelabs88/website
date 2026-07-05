## Qué es la memoria standby

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
