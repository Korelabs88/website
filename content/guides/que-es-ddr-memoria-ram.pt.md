## O que é DDR (Double Data Rate)

**DDR** significa *Double Data Rate*: a memória transfere dados **duas vezes por ciclo de clock** (na subida e na descida). Por isso um módulo DDR4 "3200 MHz" usa barramento de 1600 MHz, mas taxa efetiva de 3200 MT/s.

É a **RAM** do seu PC — o que o Windows mostra em Configurações → Sistema → Memória e no Gerenciador de Tarefas. Não confunda com VRAM da placa de vídeo ou armazenamento SSD.

### Para que serve na prática

- Manter programas, abas e arquivos abertos prontos para a CPU
- Cachear dados que o processador precisa na hora
- Reduzir acessos ao disco (muito mais lento)

Mais RAM e mais velocidade significam multitarefa e jogos mais fluidos — até certo ponto.

## Por que existem 5 gerações?

São **cinco padrões sucessivos** para PCs de consumo:

| Geração | Época aprox. | Destaque |
|---------|--------------|----------|
| **DDR** (DDR1) | 2000–2005 | Primeira DDR de consumo; substituiu SDRAM |
| **DDR2** | 2005–2010 | Menor voltagem, mais densidade |
| **DDR3** | 2010–2015 | Menos consumo; até ~2133 MT/s |
| **DDR4** | 2015–2021 | Grande salto de banda |
| **DDR5** | 2021–atual | Dois canais por módulo, mais GB por pente |

**Não são compatíveis entre si**: cada geração usa slot, voltagem e sinais diferentes. Não dá para encaixar DDR4 em placa só DDR5. Upgrades devem combinar com placa-mãe e processador.

### Por que não pararam em uma só?

Cada salto atende necessidades reais:

1. **Mais largura de banda** para CPUs e GPUs mais rápidas
2. **Menor consumo** (notebooks e servidores)
3. **Módulos maiores** (32–64 GB por pente no DDR5)
4. **Novos recursos** (DDR5: PMIC no módulo, canais duplos)

Quando uma geração não alimenta os processadores novos, a JEDEC define a próxima.

## DDR5 hoje vs DDR4

- Velocidades a partir de 4800 MT/s (vs 2133–3200 típicos no DDR4)
- Melhor eficiência energética por bit
- Maior capacidade por módulo
- Ideal para jogos modernos, edição de vídeo e muito uso de RAM

DDR4 ainda é válido se você já tem. DDR5 faz sentido em PCs novos ou upgrade completo de plataforma.

## Quando chegará o DDR6?

Em **meados de 2026** **não há padrão DDR6 publicado** nem módulos de varejo. O setor já trabalha nisso:

- **JEDEC** e fabricantes (Samsung, SK Hynix, Micron) desenvolvem a especificação
- Estimativas públicas apontam **definição do padrão em 2026–2027**, com **produtos em massa anos depois** (como no DDR5)

**DDR6 não está na esquina para o PC que você compraria hoje**, mas é o próximo passo lógico.

### Cronograma realista

| Fase | Quando (estimativa) |
|------|---------------------|
| Rascunho / spec JEDEC | 2026–2027 |
| Primeiros módulos enterprise | ~2027–2028 |
| Placas de consumo a preço razoável | 2028–2030+ |

Datas mudam com demanda de IA em servidores e capacidade de fábrica.

## Possíveis vantagens do DDR6 sobre o DDR5

Até a JEDEC fechar o padrão, parte disso é **expectativa**, não número final:

### 1. Mais largura de banda

Mais **MT/s** para CPUs multi-core e cargas pesadas (incluindo IA).

### 2. Menos energia por bit

Voltagem e gestão de energia no módulo tendem a melhorar a cada geração.

### 3. Maior densidade

Mais **GB por módulo** sem encher todos os slots — útil para 64–128 GB.

### 4. Confiabilidade / ECC

**Correção de erros on-die** mais forte para uso 24/7.

### 5. Alinhamento com plataformas futuras

DDR6 acompanhará **Intel/AMD** futuros ainda não vendidos no varejo.

**Importante:** DDR6 não substitui **RAM suficiente** nem um Windows bem administrado. Um PC com 16 GB DDR5 bem gerido pode ir melhor que um com 32 GB cheio de processos.

## O que fazer com sua RAM hoje

DDR3, DDR4 ou DDR5:

1. Veja uso de RAM em repouso (Configurações ou **Optimus** ao vivo)
2. Feche apps em segundo plano inúteis
3. Se faltar RAM, **amplie com a mesma geração** antes de trocar tudo
4. Libere memória **standby** com segurança antes de jogar ou renderizar

**Optimus** monitora RAM, CPU e disco em tempo real e pode purgar standby com operações nativas do Windows — grátis e local.

## Perguntas frequentes

**DDR é igual a SDRAM?** Não. SDRAM veio antes; DDR é a evolução de taxa dupla desde ~2000.

**Posso misturar marcas?** Geralmente sim, se geração, voltagem e velocidade coincidirem. Pares idênticos são melhores para dual channel.

**Mais MHz é sempre melhor?** Só se placa e CPU suportarem. Frequências fora do spec podem não ligar.

**DDR6 vai obsoletar DDR5 na hora?** Não. Transições levam anos; DDR4 ainda é comum em 2026.

**Optimus acelera o hardware DDR?** Não. Otimiza **como o Windows usa** a memória que você já tem.
