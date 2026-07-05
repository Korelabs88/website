## Por que o Windows fica sem RAM

O Windows gere memória de forma agressiva: mantém arquivos e apps recentes na **lista standby** para abrir mais rápido. Não é erro, mas ao abrir jogos ou apps pesados você pode ficar sem RAM disponível.

Muitos "otimizadores" mostram porcentagem falsa ou liberam memória que o Windows recupera na hora. O que funciona é agir sobre **working sets**, **standby** e **modified** com APIs nativas.

## Métodos que funcionam

### 1. Fechar apps não usadas
O Gerenciador de Tarefas (Ctrl+Shift+Esc) mostra o que mais consome RAM.

### 2. Revisar programas de inicialização
Menos apps na boot = mais RAM livre desde o início. Optimus inclui gestão de inicialização.

### 3. Liberação real com Optimus
**Optimus** executa operações documentadas do Windows: esvaziar working sets, purgar standby, descarregar modified e limpar cache do sistema (opcional, admin).

Mede antes/depois com detalhamento. Sem telemetria ou assinatura.

## O que evitar

- Programas que prometem "50% mais RAM" com animações falsas
- Serviços online com acesso remoto ao PC

## Passos recomendados

1. Baixe Optimus
2. Execute como administrador se necessário
3. Abra o módulo RAM
4. Selecione operações e confirme
5. Compare no monitor ao vivo

## FAQ

**Liberar RAM prejudica o Windows?** Não, com operações reversíveis como as do Optimus.

**É grátis?** Sim. Optimus é gratuito e local.
