Aconteceu com você, ou com algum amigo — com certeza. Você atualiza o setup, liga o contador de FPS no canto da tela, e lá está: 280, 300, às vezes picos de 340. Um número que anos atrás só se via em configs de laboratório para benchmark. Você deveria estar vivendo a experiência gamer mais fluida da sua vida.

E mesmo assim algo está errado. O jogo sente entrecortado. Micro-travamentos aparecem do nada, sobretudo nos momentos mais intensos: explosão grande, giro brusco de câmera, o instante exato em que precisa reagir rápido ou morrer. Olha o contador — 290 FPS — e pensa: "como pode sentir mal se o número é altíssimo?"

Bem-vindo a uma das maiores mentiras que a cultura de benchmark nos vendeu: que FPS médio é sinônimo de fluidez. Não é. Entender por quê muda completamente como você avalia o desempenho do PC.

## A média é maquiagem estatística

Pense no FPS médio como salário médio de uma empresa. Se nove pessoas ganham normal e uma (o dono) ganha uma fortuna, a "média" da empresa fica alta e enganosa. Não representa a realidade da maioria.

O FPS médio funciona igual. Se o jogo roda a 400 FPS nos momentos tranquilos (olhando parede, parado no spawn) e cai para 60 FPS na ação real (combate, muitos efeitos, explosões), a média final pode continuar em 290 FPS — embora a experiência quando importa de verdade (jogando de fato, não olhando parede) seja bem pior do que o número sugere.

A média mente porque mistura o fácil de renderizar com o difícil, deixando o fácil "tapar" o difícil.

| Métrica | O que mede | Reflete fluidez real? |
|---------|------------|------------------------|
| **FPS médio** | Média da sessão | **Não** — esconde vales |
| **1% low** | Pior 1% dos frames | **Sim** — seus piores momentos |
| **0,1% low** | Pior 0,1% dos frames | **Sim** — micro-travamentos extremos |
| **Frame time (ms)** | Milissegundos por frame | **Sim** — o que sente ao mover câmera |

## O verdadeiro herói: 1% low

O **1% low** (e o primo mais rigoroso **0,1% low**) não mede a média geral — mede **desempenho no pior 1% dos frames gerados**. Em vez de "como foi no geral?", pergunta "quão mal foi nos piores momentos?".

Essa métrica é muito mais honesta sobre como jogar *sente*, porque seu cérebro não percebe média de sessão. Percebe picos e vales. Um travão de meio segundo no instante em que ia reagir a um inimigo custa a partida — não o fato de dois segundos antes estar a 350 FPS olhando o céu.

Exemplo concreto: dois PCs, mesmo jogo.

**PC A**: 240 FPS médio. 55 FPS de 1% low.

**PC B**: 165 FPS médio. 130 FPS de 1% low.

No papel, PC A "ganha" por margem enorme se só olhar média. Mas jogando, PC B sente dramaticamente mais consistente, previsível, "suave" nos momentos críticos. PC A tem picos espetaculares seguidos de quedas bruscas que parecem tropeços. PC B mantém piso muito mais estável embora o teto seja menor.

Quase qualquer jogador competitivo, testando às cegas sem ver números, escolheria PC B como "mais fluido" apesar da média menor.

## Por que acontecem quedas se o hardware é potente?

Várias causas típicas — cada uma com solução diferente:

**1. Stutter de compilação de shaders.**

Muitos jogos modernos compilam shaders na primeira vez que o efeito aparece, não antes. Gera micro-travamentos quando surge efeito novo (explosão com partículas que você não viu na sessão) — não importa quão potente o hardware. Alguns jogos pré-compilam ao iniciar; outros não.

**2. Falta de margem de RAM ou VRAM nos picos.**

Como vimos em **sua RAM não está "cheia", está trabalhando**, quando o sistema precisa reorganizar memória de repente (muitos efeitos numa explosão grande), essa reorganização causa pausa perceptível — mesmo com FPS médio altíssimo.

**3. Processos em segundo plano acordando no pior momento.**

Antivírus agendado, Windows Update baixando, Discord processando notificação com imagem — competição curta por recursos no momento mais intenso não derruba muito a média, mas destrói o 1% low.

**4. Limitações de CPU em cenas com muita lógica simultânea.**

Explosão grande não é só visual: física, hitboxes, áudio posicional, IA reagindo. Carga de golpe pode derrubar frames mesmo com CPU ociosa o resto do tempo.

| Causa da queda | Sintoma típico | O que testar |
|---------------|----------------|--------------|
| Shaders sem compilar | Travão na 1ª vez que vê efeito | Pré-compilar shaders / rodada de aquecimento |
| RAM/VRAM no limite | Stutter em combate + disco ativo | Fechar apps, liberar standby, mais RAM/VRAM |
| Background | Travões aleatórios | Modo gamer, fechar overlays, adiar updates |
| Limite de CPU | GPU com folga, 1% low baixo em multidões | CPU melhor ou settings que carregam lógica |

## O erro de "otimizar para o número"

Aqui está o coração da paradoja. Muita gente obceca em subir FPS médio: baixar gráficos, mods de desempenho — tudo para ver número maior no canto. Às vezes conseguem: média sobe de 220 para 280.

Mas se isso não ataca a causa real das quedas pontuais (shaders, memória sem margem, background competindo), o 1% low continua ruim ou piora — agora mais frames "fáceis" estatisticamente tapam os mesmos frames "difíceis".

É como melhorar velocidade média do corredor nos trechos planos sem consertar cair em cada buraco. Média melhora no papel. Correr aquela pista com buracos intactos continua ruim.

Relacionado: ativar DLSS para subir média sem melhorar lows é a mesma armadilha ao contrário — às vezes upscale melhora ambos; às vezes só infla número em cenas fáceis. Veja nosso guia sobre **DLSS e FSR vs resolução nativa** (link no final).

## Então, que número olhar em vez da média?

Se quer experiência que *sinta* fluida, não só "meça bem" em screenshot com contador, priorize:

**1. 1% low como referência principal**, não média. MSI Afterburner, CapFrameX ou overlay de muitos jogos mostram direto.

**2. Consistência do frame time** mais que número puro. Gráfico de frame time relativamente plano vale mais que picos altos e vales profundos com mesma média.

**3. Como sente nos momentos de maior exigência real**, não menu ou spawn. Vá direto à zona de combate mais caótica e avalie lá.

### Checklist rápido antes de culpar hardware

1. Meça **1% low** em combate real, não menu
2. Pré-compile shaders se o jogo permitir
3. Feche background pesado; **modo gamer do Optimus** antes de ranked
4. Verifique RAM e VRAM no pico (Gerenciador de Tarefas / Afterburner)
5. Drivers GPU atualizados

Para entender o que limita seu PC (CPU, GPU, RAM, disco), veja o guia sobre **como RAM, GPU, CPU e disco afetam jogos** (link no final).

## Perguntas frequentes

**Quanto de 1% low é "bom"?** Depende do jogo e refresh do monitor. Regra prática: 1% low não cair muito abaixo de ~80% do refresh (ex.: 144 Hz, ideal lows >115 FPS). Em 60 Hz, lows estáveis >50 FPS já sentem bem.

**Cap a 141 FPS ajuda fluidez?** Às vezes: limitar FPS estabiliza frame pacing em alguns títulos. Teste com V-Sync off + cap no Afterburner.

**Mais FPS sempre = menos input lag?** Em geral sim até certo ponto, mas se lows são lixo, input sente inconsistente apesar da média alta.

**Optimus sobe 1% low?** Não overclocka. Libera RAM e reduz ruído de fundo — útil se lows vêm de memória ou processos competindo, não GPU pura.

**Frame Generation (DLSS 3) melhora lows?** Sobe FPS perceptível mas pode adicionar latência; em competitivo priorize lows reais sem geração de frames.

## A lição real

Número grande no canto é viciante, fácil de comparar com amigos, fácil de vender no marketing de GPU nova. Mas não é o que seu cérebro lê como "jogar bem". Seu cérebro lê consistência. Que ao girar câmera a imagem responde sem surpresas. Que no instante exato da explosão o jogo não trai com meio segundo de pausa quando você precisa reagir mais rápido que nunca.

Na próxima vez que avaliar se o PC "vai bem" ou precisa upgrade, pare de olhar só média. Olhe piores momentos, não melhores. Nos jogos como na vida, não se lembra da média de uma noite. Lembra do instante exato em que algo deu errado.

E esse instante não mede FPS médio. Mede 1% low.
