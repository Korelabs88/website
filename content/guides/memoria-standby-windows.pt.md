## O que é memória standby

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
