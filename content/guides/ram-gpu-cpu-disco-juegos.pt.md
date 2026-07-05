## Resposta rápida: quem afeta o quê?

| Componente | Afeta principalmente… | Impacto típico no jogo |
|------------|----------------------|------------------------|
| **GPU** | FPS, qualidade visual, resolução | **Muito alto** |
| **CPU** | FPS mínimos, simulações, muitos NPCs | **Alto** (depende do jogo) |
| **RAM** | Stutter, fechamentos, Discord + jogo | **Médio** (se faltar ou estiver cheia) |
| **Disco** | Tempo de carga, streaming de texturas | **Baixo no FPS**; **alto nas cargas** |

Não há um único rei: competitivo 1080p pode ser **limitado pela CPU**; AAA em 4K, pela **GPU**; com 8 GB cheios, tudo engasga.

## GPU: o motor dos frames

A **placa de vídeo** desenha cada frame: shaders, texturas, efeitos. Em 1440p/4K, a GPU costuma ser o **primeiro gargalo** ao subir qualidade ou FPS.

### O que importa na GPU

- **VRAM**: 8 GB muitas vezes bastam em 1080p/1440p; 12–16 GB ajudam em 4K e mods pesados. VRAM cheia = stutter.
- **Potência bruta**: quantos FPS você segura em X resolução.
- **Drivers atualizados**: às vezes +10 % só instalando do fabricante.

### Sinais de limite na GPU

- GPU ~95–100 % no jogo, CPU mais baixa
- Baixar resolução ou qualidade **sobe muito** o FPS
- Monitoramento mostra GPU no limite

**Optimus** não substitui GPU melhor, mas **modo gamer** e liberar RAM ajudam a CPU alimentar a placa.

## CPU: o maestro

O **processador** prepara a cena: física, IA, animações. Jogos **single-thread** querem núcleos rápidos; estratégia e simuladores usam **mais núcleos**.

### Quando a CPU limita mais que a GPU

- Shooters competitivos em **1080p alto FPS**
- Cidades densas em **Cyberpunk**, **Starfield**
- Emulação, Minecraft com mods

### Sinais de gargalo na CPU

- GPU a 60–70 % e **um núcleo** a 100 %
- 1 % lows ruins com média OK
- Subir gráficos **quase não muda** FPS

Mais núcleos nem sempre ajudam; **GHz** e arquitetura recente importam.

## RAM: capacidade, velocidade e memória cheia

A **RAM** guarda jogo, texturas, Discord, navegador e Windows. Sem RAM livre, o sistema usa disco e aparecem **travadas**.

### Capacidade confortável (2026)

| Uso | Mínimo confortável |
|-----|-------------------|
| Jogos casuais + Windows | 16 GB |
| AAA + Discord + browser | **32 GB** |
| 4K, mods, streaming | 32–64 GB |

**8 GB** hoje é apertado para muitos títulos.

### Velocidade DDR

- DDR4 3200 vs 3600: often **1–5 %** de diferença
- O crítico é **ter o suficiente**, não os últimos MHz

### RAM cheia vs standby

Feche abas e launchers; purgue standby se estiver no limite (**Optimus** com operações nativas).

### Sinais de problema de RAM

- Uso **>90 %** constante com disco ativo
- Fechamentos inesperados
- Stutter em open world com GPU ociosa

## Disco: HDD, SATA SSD e NVMe

Armazenamento **quase não muda FPS** em combate estável após carregar. Nota-se em:

| Tipo | Cargas | Streaming open world | FPS combate |
|------|--------|----------------------|-------------|
| **HDD** | Lentas | Pops ao girar | Similar* |
| **SATA SSD** | Rápidas | Muito bom | Referência |
| **NVMe** | Muito rápidas | Excelente | ~igual SATA |

Instale jogos em **SSD**; mantenha **20 %+ livre** no disco do sistema.

## Como interagem

```
Disco → carrega nível na RAM
RAM → CPU processa lógica
CPU → manda trabalho à GPU
GPU → desenha o frame
```

Disco lento → cargas longas.
RAM falta → paging.
CPU fraca → GPU espera.
GPU fraca → FPS baixo com GPU a 100 %.

## O que melhorar primeiro?

| Sintoma | Prioridade |
|---------|------------|
| FPS baixo em 4K / ultra | GPU |
| FPS instável 1080p competitivo | CPU (+ RAM se <16 GB) |
| Cargas eternas | SSD / NVMe |
| Micro-travadas, crashes | RAM |
| PC velho no geral | Plataforma nova |

## Ajustes grátis

1. Drivers GPU
2. Plano alto desempenho (notebook na tomada)
3. Fechar overlays
4. **Modo gamer Optimus** + liberar standby
5. Jogo no SSD
6. Presets realistas

## FAQ

**32 GB dão mais FPS que 16 GB?** Só se 16 GB não bastavam.

**NVMe vs SATA no Fortnite?** Quase igual em FPS; NVMe ganha na carga.

**Optimus sobe FPS?** Não overclocka GPU; limpa sistema e RAM.

## Conclusão

- **GPU** → visual e FPS médio
- **CPU** → mínimos e jogos pesados em lógica
- **RAM** → fluidez quando falta
- **Disco** → cargas e streaming

Meça antes de comprar. **Optimus** ajuda em RAM, disco e modo gamer — grátis no Windows 10/11.
