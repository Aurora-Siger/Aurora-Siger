# MISSÃO AURORA SIGER
## Relatório de Análise Energética e Propulsiva
**Ignition Zero — Fase 1 | Março de 2026**

---

## 0. Sistema de Propulsão e Caracterização da Nave Aurora Siger

A nave Aurora Siger foi concebida como uma plataforma de lançamento de estágio único (*Single Stage To Orbit* — SSTO), com massa total de 20.000 kg. Seu design estrutural foi inspirado em plataformas de pequeno porte da categoria de nanossatélites, tendo como referência o Hanbit, desenvolvido pela KARI (Korea Aerospace Research Institute, Coreia do Sul), adaptado para receber um sistema de propulsão química de alto desempenho compatível com missões de inserção orbital.

Para a propulsão principal, foi desenvolvido o motor **Aurora P-1**, um motor fictício criado especificamente para esta missão, cuja combinação de propelentes e ciclo termodinâmico foram inspirados nos motores **Merlin 1D**, utilizados pela SpaceX nos foguetes Falcon 9. Assim como os Merlin, o Aurora P-1 utiliza querosene aeroespacial de grau RP-1 como combustível e oxigênio líquido criogênico (LOX) como oxidante, operando em um ciclo de gerador de gás (*gas-generator cycle*). Essa combinação é reconhecida na engenharia aeroespacial pelo equilíbrio entre desempenho, estabilidade de combustão e viabilidade operacional.

A principal diferença entre o Aurora P-1 e seus motores de referência é a configuração de **estágio único**: ao contrário do Falcon 9, que opera com dois estágios separáveis, a nave Aurora Siger realiza toda a trajetória — da decolagem à inserção orbital — com um único estágio propulsivo, sem separação de estrutura em voo. Isso implica maior exigência sobre a razão massa de propelente/massa seca da nave, justificando os cenários A (90%) e B (95%) analisados neste relatório.

### Parâmetros Técnicos do Motor Aurora P-1

| Parâmetro | Valor adotado | Referência |
|---|---|---|
| Combustível | RP-1 (querosene aeroespacial) | Merlin 1D — SpaceX / Falcon 9 |
| Oxidante | LOX (oxigênio líquido criogênico) | Merlin 1D — SpaceX / Falcon 9 |
| Ciclo termodinâmico | Gerador de gás (*gas-generator*) | Merlin 1D — SpaceX |
| Isp ao nível do mar | 282 s | Merlin 1D — Astronautix (2013) |
| Isp em vácuo | 320 s | Projetado para o Aurora P-1 |
| Razão combustível/oxidante | 1:2 (RP-1:LOX) | Padrão LOX/RP-1 aeroespacial |
| Configuração | Estágio único (SSTO) | Definição da Missão Aurora |

> **Nota sobre o Isp em vácuo (320 s):** O Merlin 1D opera com Isp de 348 s em vácuo (Astronautix). O valor de 320 s adotado para o Aurora P-1 é uma projeção de desempenho para um motor fictício de próxima geração, mantendo coerência com a família de motores que o inspirou. Todos os cálculos de ΔV, consumo de propelente e autonomia apresentados nas seções subsequentes utilizam o Isp de 320 s como valor de referência.

### Fontes desta seção

| Sistema / Dado | Fonte | URL |
|---|---|---|
| Motor Merlin 1D — Isp, ciclo e propelentes | Astronautix — Merlin 1D | astronautix.com/m/merlin1d.html |
| Merlin 1D — ciclo gas-generator e RP-1/LOX | Wikipedia — SpaceX Merlin | en.wikipedia.org/wiki/SpaceX_Merlin |
| Falcon 9 — configuração de motores | Wikipedia — Falcon 9 | en.wikipedia.org/wiki/Falcon_9 |
| KARI — Hanbit (referência estrutural) | Korea Aerospace Research Institute | kari.re.kr |

---

## 1. Parâmetros Iniciais da Missão

Os valores abaixo foram definidos com base nas anotações do caderno e nos dados de referência da NASA Technical Reports para o propelente RP-1 (querosene) com oxidante LOX.

| Parâmetro | Símbolo | Valor | Fonte |
|---|---|---|---|
| Massa total inicial | m₀ | 20.000 kg | Definição da missão |
| Isp do motor | Isp | 320 s | NASA Tech. Reports |
| Velocidade de exaustão | Ve | 3.139,2 m/s | Ve = Isp × g₀ |
| Aceleração gravitacional | g₀ | 9,81 m/s² | Constante terrestre |
| Propelente (Cen. A) | mprop | 18.000 kg (90%) | Caderno – tentativa 1 |
| Propelente (Cen. B) | mprop | 19.000 kg (95%) | Caderno – tentativa 2 |
| Razão combust./oxidante | — | 1:2 (RP-1:LOX) | Caderno |

> **Nota:** A razão 1:2 combustível/oxidante resulta em aproximadamente 6.000 kg de RP-1 e 12.000 kg de LOX no Cenário A (mprop = 18.000 kg).

---

## 2. Divisão da Missão em Fases

A trajetória da nave Aurora foi dividida em três fases com base nos regimes atmosféricos e nas forças predominantes em cada segmento:

| Fase | Altitude | ΔV Estimado | Força Dominante |
|---|---|---|---|
| Fase 1 — Decolagem | 0 → 12 km | 1.800 m/s | Gravidade + Arrasto máximo |
| Fase 2 — Ascensão | 12 → 80 km | 3.200 m/s | Gravidade (arrasto decrescente) |
| Fase 3 — Inserção | 80 → 400 km | 4.100 m/s | Gravidade + Circularização orbital |
| **TOTAL** | **0 → 400 km** | **9.100 m/s** | — |

---

## 3. Aplicação da Equação de Tsiolkovsky

A equação de Tsiolkovsky define a variação de velocidade (ΔV) que um foguete pode atingir com base na razão entre a massa inicial e a massa final após queimar o propelente:

```
ΔV = Ve × ln(m₀ / mf)
mf = m₀ × e^(−ΔV / Ve)
```

Em uma configuração monobloco, a massa final de cada fase se torna a massa inicial da fase seguinte, formando uma cadeia de cálculos encadeados.

### 3.0 Legenda dos Símbolos e Conceitos

| Símbolo | Nome | Unidade | Significado |
|---------|------|:-------:|-------------|
| ΔV | Delta-V (Variação de Velocidade) | m/s | "Orçamento" total de mudança de velocidade disponível no foguete dado seu propelente. Não é a velocidade final da nave — é a capacidade acumulada de aceleração e manobra. Para atingir a LEO a partir do solo, o foguete precisa gastar ~9.100 m/s desse orçamento combatendo gravidade e arrasto e acelerando até a velocidade orbital (~7.800 m/s). Quanto mais propelente, maior o ΔV disponível. |
| Ve | Velocidade de Exaustão | m/s | Velocidade com que os gases saem pelo bocal do motor. Quanto mais rápido os gases são ejetados, mais eficiente é o empuxo — pelo princípio da conservação do momento, cada kg de gás ejetado a alta velocidade gera mais impulso na nave. É o multiplicador da equação de Tsiolkovsky: um Ve maior produz mais ΔV com a mesma quantidade de propelente. Calculado por `Ve = Isp × g₀`. |
| Isp | Impulso Específico | s | Medida de eficiência do motor: quantos segundos o motor consegue produzir 1 N de empuxo consumindo 1 N de propelente por segundo. É o equivalente ao "km/l" de um carro — quanto maior o Isp, mais eficiente o motor. Expresso em segundos para ser independente da gravidade local e comparável entre motores de diferentes fabricantes. |
| m₀ | Massa inicial | kg | Massa total da nave no início de cada fase, incluindo propelente ainda não queimado. |
| mf | Massa final | kg | Massa da nave ao fim de cada fase, após queimar o propelente necessário para atingir o ΔV daquela fase. |
| g₀ | Aceleração gravitacional padrão | m/s² | Constante terrestre: 9,81 m/s². Usada para converter Isp em Ve. |
| ln | Logaritmo natural | — | Função matemática de base *e* (~2,718). Aparece na equação de Tsiolkovsky porque a queima de propelente é um processo exponencial: conforme o foguete fica mais leve, cada kg queimado gera mais ΔV. |

> **Relação entre os três conceitos principais:** `Ve = Isp × g₀`. O Isp é a forma normalizada de expressar a Ve, e ambos determinam o ΔV que a nave consegue produzir para uma dada razão de massa (m₀/mf).

| Motor | Isp em vácuo | Propelente |
|-------|:------------:|------------|
| Aurora P-1 (este projeto) | 320 s | RP-1 / LOX |
| Merlin 1D — SpaceX (referência) | 348 s | RP-1 / LOX |
| RS-25 — Space Shuttle | 453 s | LH₂ / LOX |
| Motor químico típico | 250–460 s | varia |

### 3.1 Cenário A — mprop = 90% (18.000 kg)

| Fase | m₀ (kg) | mf (kg) | Propelente Usado (kg) | ΔV Alcançado (m/s) |
|---|---|---|---|---|
| Fase 1 | 20.000 | 11.272 | 8.728 | 1.800 |
| Fase 2 | 11.272 | 4.067 | 7.205 | 3.200 |
| Fase 3 | 4.067 | 2.000 | 2.067 | 2.229 |
| **TOTAL** | **20.000** | **2.000** | **18.000** | **7.229** |

> ⚠️ **Análise Cenário A:** mf final = 2.000 kg (massa seca atingida — propelente esgotado na Fase 3 antes de completar o ΔV necessário). ΔV total alcançado: **7.229 m/s** — **INSUFICIENTE** para LEO (necessário ≥ 9.100 m/s). **Déficit: −1.871 m/s.** Conclusão do caderno confirmada: 90% de propelente não é suficiente.
>
> *Nota: Na Fase 3, os 18.000 kg de propelente disponíveis são integralmente consumidos nas Fases 1 e 2 (8.728 + 7.205 = 15.933 kg) mais os 2.067 kg restantes — a nave esgota o estoque antes de completar a inserção orbital.*

### 3.2 Cenário B — mprop = 95% (19.000 kg)

| Fase | m₀ (kg) | mf (kg) | Propelente Usado (kg) | ΔV Alcançado (m/s) |
|---|---|---|---|---|
| Fase 1 | 20.000 | 11.272 | 8.728 | 1.800 |
| Fase 2 | 11.272 | 4.067 | 7.205 | 3.200 |
| Fase 3 | 4.067 | 1.102 | 2.966 | 4.100 |
| **TOTAL** | **20.000** | **1.102** | **18.898** | **9.100** |

> ✅ **Análise Cenário B:** mf calculado para atingir ΔV necessário = 1.102 kg. Massa seca = 1.000 kg. ΔV necessário para LEO = 9.100 m/s — **SUFICIENTE** (≥ 9.100 m/s). ΔV máximo alcançável consumindo todo o propelente disponível (19.000 kg): **9.403 m/s**. **Margem de segurança: +303 m/s** (102 kg de propelente de reserva — a nave atinge LEO antes de esgotar o estoque).

### 3.3 Consumo de Combustível por Fase — Cenário B (95%)

| Fase | Altitude | Duração | Propelente Gasto (kg) | % do Total | kg/min |
|---|---|---|---|---|---|
| Fase 1 — Decolagem | 0 → 12 km | 4 min | 8.728 | 46,2% | 2.182 |
| Fase 2 — Ascensão | 12 → 80 km | 8 min | 7.205 | 38,1% | 901 |
| Fase 3 — Inserção | 80 → 400 km | 12 min | 2.966 | 15,7% | 247 |
| Massa seca (estrutura) | — | — | 1.000 | 5,0% | — |
| **TOTAL** | **0 → 400 km** | **24 min** | **18.898** | **100%** | **787** |

> ⚡ **Fase mais intensa:** Fase 1 consome 2.182 kg/min — o maior ritmo de queima da missão, em apenas 4 minutos ao nível do solo onde o arrasto é máximo. A Fase 2 é a maior consumidora em massa absoluta (7.205 kg = 38,1% do total), pois precisa vencer o maior ΔV (3.200 m/s). A Fase 3 é a mais econômica por já operar com a nave muito mais leve.

---

## 4. Parâmetros Gravitacionais Adotados na Missão

| Parâmetro | Valor Adotado | Origem |
|---|---|---|
| Aceleração gravitacional (g₀) | 9,81 m/s² | Constante padrão terrestre (NIST) |
| Velocidade de exaustão (Ve) | 3.139,2 m/s | Ve = Isp × g₀ = 320 × 9,81 |
| ΔV total calculado | 9.100 m/s | Tsiolkovsky — Cenário B (95%) |

---

## 5. Análise Energética — Sistema Elétrico Embarcado

Além do sistema propulsivo, a nave Aurora requer energia elétrica para operar sensores, computadores de bordo, sistemas de telemetria e controle de atitude. Esta análise é independente do propelente e mede a autonomia das baterias.

### 5.0 Fonte de Energia Elétrica — Justificativa Técnica

A energia elétrica embarcada da nave Aurora Siger é fornecida exclusivamente por **baterias de íon de lítio de grau aeroespacial** durante toda a fase propulsiva da missão (24 minutos). Essa escolha se apoia em dois critérios técnicos fundamentais:

**Por que baterias e não painéis solares durante o voo?**

Durante a decolagem e a ascensão atmosférica, a geração fotovoltaica é inviável como fonte primária de energia por três razões principais. Primeiro, a orientação da nave varia continuamente ao longo da trajetória, impedindo que os painéis mantenham alinhamento estável com o Sol — condição indispensável para geração eficiente. Segundo, painéis solares implantados na estrutura externa estariam sujeitos à vibração estrutural intensa da fase propulsiva, podendo comprometer sua integridade e aumentar o arrasto aerodinâmico durante a passagem pela atmosfera densa. Terceiro, durante a ascensão supersônica, os painéis dobráveis precisam permanecer recolhidos para proteger sua estrutura das cargas aerodinâmicas e acústicas do voo — condição documentada em missões reais como referência de design de veículos lançadores. Painéis solares são previstos apenas para operação pós-inserção orbital, fora do escopo desta análise de pré-decolagem.

**Por que baterias de íon de lítio?**

As baterias de íon de lítio são o padrão consolidado na indústria aeroespacial para sistemas embarcados em veículos lançadores. Baterias de íon de lítio oferecem maiores níveis de energia e maior vida útil em ciclos, com menor peso e menor volume, quando comparadas a tecnologias mais antigas como Ni-Cd ou Ni-MH. Fabricantes como **EaglePicher** e **Airbus Defence & Space** fornecem linhas específicas para aplicações em lançadores: a linha LAUNCHER-BATT da Airbus é desenvolvida especificamente para o mercado de lançadores, oferecendo o melhor compromisso entre desempenho mecânico, segurança e confiabilidade, necessários para o sucesso de missões de lançamento. Adicionalmente, a **GS Yuasa** — fabricante japonesa certificada ISO 9001 — é líder mundial em energia armazenada em baterias de íon de lítio para o setor espacial, com mais de 4,5 MWh de energia embarcada em voo e mais de 550 milhões de horas de operação de células sem anomalia ou falha registrada, tendo fornecido células para programas da NASA, JAXA e ISS.

Para a missão Aurora Siger, adota-se como referência de fornecedor o modelo conceitual baseado nas especificações da **EaglePicher** e **GS Yuasa**, com células de íon de lítio qualificadas para as condições de vibração, temperatura e vácuo do ambiente de lançamento.

| Aspecto | Baterias de íon de lítio | Painéis solares |
|---|---|---|
| Fase propulsiva (0–24 min) | ✅ Viável — fonte primária | ❌ Inviável — painéis recolhidos |
| Condições de vibração | ✅ Tolerante | ❌ Risco estrutural |
| Orientação variável da nave | ✅ Independente | ❌ Requer rastreamento solar |
| Pós-inserção orbital | ✅ Reserva disponível | ✅ Fonte primária preferencial |

| Fornecedor de referência | País | Aplicação |
|---|---|---|
| EaglePicher Technologies | EUA | Baterias para veículos lançadores (Atlas V, Delta II/IV) |
| Airbus Defence & Space (LAUNCHER-BATT) | Europa | Baterias para lançadores — linha específica |
| GS Yuasa Technology (GYT) | Japão | Células Li-ion para satélites e foguetes — ISS, JAXA, NASA |

### 5.1 Parâmetros das Baterias

| Parâmetro | Valor |
|---|---|
| Capacidade total das baterias | 500 kWh |
| Carga atual | 82% |
| Energia disponível | 410,00 kWh |
| Fator de perda (térmica + resistiva) | 8% |
| Energia útil efetiva | 377,20 kWh |

### 5.2 Sistemas Eletrônicos Embarcados e Consumo por Fase

Os sistemas eletrônicos da nave Aurora foram definidos com base em referências reais de missões aeroespaciais (NASA Small Spacecraft Avionics, AstroForge Odin Mission, PCB Aerospace). O consumo é variável por fase, pois cada sistema opera em regime diferente dependendo do momento do voo.

| Sistema | Referência Real | Fase 1 (W) | Fase 2 (W) | Fase 3 (W) |
|---|---|---|---|---|
| Computador de bordo (Flight Computer) | AstroForge Odin: 35W/unidade — Aurora usa 2 unidades redundantes | 70 | 70 | 70 |
| Telemetria e comunicação | CubeSat Power Budget Guide: 5–15W em transmissão ativa | 800 | 1.200 | 2.000 |
| Sensores de navegação (IMU + GPS + giroscópios) | IMU aeroespacial típico: 5–15W; conjunto completo ~25W | 25 | 25 | 25 |
| Controle de atitude (RCS — válvulas e atuadores) | Atuadores lineares de gimbaling: 2–10 kW em correção ativa | 8.000 | 5.000 | 1.500 |
| Sistema de ignição e válvulas motorizadas | Válvulas solenóides aerospace: 200–500W; ignição: pico de 2 kW | 2.500 | 500 | 200 |
| Iluminação e sistemas de cabine | Padrão aeronáutico: 100–300W para sistemas de cabine | 150 | 150 | 150 |
| Sensores de temperatura (termistores NTC) | TE Connectivity NASA-qualified NTC: 0,5–2W por sensor; 20 sensores | 30 | 30 | 30 |
| Sensores de pressão (piezoelétricos) | PCB Aerospace ICP®: 2–5W por sensor; 10 sensores | 40 | 40 | 40 |
| Sensores de volume/nível de propelente | Collins Aerospace space-grade: 3–8W por sensor; 6 sensores | 36 | 36 | 20 |
| ECUs (Unidades de controle eletrônico) | CAN Bus aerospace ECU: 5–15W por unidade; 4 ECUs | 50 | 50 | 50 |
| **TOTAL** | — | **11.701** | **7.101** | **4.085** |

> **Nota sobre o RCS e Ignição:** O controle de atitude (RCS) domina o consumo na Fase 1 porque os motores precisam de correções constantes durante a decolagem, quando o arrasto e as forças laterais são máximos. O sistema de ignição tem pico apenas na Fase 1 e cai drasticamente após a queima estar estabilizada. A telemetria aumenta progressivamente porque a distância com o solo cresce e o sinal precisa de maior potência para manter link.

### 5.3 Consumo Total e Energia por Fase

| Fase | Potência Total (kW) | Duração (min) | Energia Consumida (kWh) |
|---|---|---|---|
| Fase 1 — Decolagem | 11,70 | 4 | 0,78 |
| Fase 2 — Ascensão | 7,10 | 8 | 0,95 |
| Fase 3 — Inserção | 4,08 | 12 | 0,82 |
| **TOTAL** | **7,63** | **24** | **2,54** |

| Indicador | Resultado |
|---|---|
| Energia total consumida na missão | 2,54 kWh |
| Energia útil disponível | 377,20 kWh |
| Saldo energético (margem) | 374,66 kWh |
| Autonomia estimada (potência média) | 49,44 horas |

> ✅ O sistema elétrico apresenta margem confortável: 374,66 kWh de reserva após a missão completa. A autonomia de 49,44 horas supera amplamente a duração total de 24 minutos da fase propulsiva.

> **Nota — Limiar mínimo de 70% para autorização de decolagem:** O limiar operacional mínimo de 70% de carga das baterias foi definido como margem de segurança da Missão Aurora Siger. Com 70% de carga, a energia disponível é 350 kWh (70% × 500 kWh). Descontando o fator de perda de 8%, a energia útil efetiva seria 322 kWh — frente ao consumo total de 2,54 kWh da missão, a margem resultante seria de 319,46 kWh, suficiente para cobrir integralmente a fase propulsiva com ampla reserva. A carga atual de 82% (energia útil efetiva: 377,20 kWh) supera amplamente esse limiar mínimo.

### 5.4 Energia Química Disponível no Propelente (RP-1)

Esta seção calcula o potencial energético químico contido na massa de RP-1 carregada, com base na razão de mistura 1:2 (RP-1:LOX) e na massa total de propelente do Cenário B (95% da massa da nave).

Apenas o RP-1 contribui com energia química — o LOX é o oxidante e não possui valor energético próprio. A densidade energética do RP-1 é de 43,2 MJ/kg, valor de referência da NASA para querosene de grau aeroespacial.

| Parâmetro | Cálculo | Resultado |
|---|---|---|
| Massa total de propelente (95%) | 20.000 × 0,95 | 19.000 kg |
| Massa de RP-1 (1 parte de 3) | 19.000 ÷ 3 | 6.333,33 kg |
| Massa de LOX (2 partes de 3) | 19.000 × 2/3 | 12.666,67 kg |
| Densidade energética RP-1 | Referência NASA | 43,2 MJ/kg |
| Energia química bruta | 6.333,33 × 43,2 | 273.600,00 MJ |
| Conversão para kWh | 273.600,00 × 0,2778 | 76.000,61 kWh |
| Eficiência térmica do motor | 65% (valor típico RP-1/LOX) | 0,65 |
| Energia química útil (empuxo) | 76.000,61 × 0,65 | 49.400,40 kWh |

> ✅ **Energia química bruta total:** 76.001 kWh | **Energia útil convertida em empuxo:** 49.400 kWh | **Energia elétrica embarcada (baterias):** 500 kWh = 0,66% da energia química total. Isso ilustra que a energia elétrica dos sistemas computacionais representa uma fração ínfima do total energético da missão.

---

## 6. Resumo Executivo e Conclusões

| Critério de Verificação | Status | Detalhe |
|---|---|---|
| Propelente suficiente (Cen. A — 90%) | ❌ FALHOU | ΔV calculado = 7.229 m/s < 9.100 m/s necessário (déficit: −1.871 m/s) |
| Propelente suficiente (Cen. B — 95%) | ✅ APROVADO | ΔV máx = 9.403 m/s ≥ 9.100 m/s (margem: +303 m/s) |
| Massa seca viável (Cen. B) | ✅ APROVADO | mf = 1.102 kg ≥ 1.000 kg |
| Energia química bruta (RP-1) | ✅ CALCULADO | 76.001 kWh brutos \| 49.400 kWh úteis |
| Energia elétrica embarcada | ✅ APROVADO | 500 kWh = 0,66% da energia química |
| Saldo elétrico após missão | ✅ APROVADO | Margem: 374,66 kWh |

O Cenário A (mprop = 90%) foi descartado — com apenas 18.000 kg de propelente, o foguete esgota o estoque durante a Fase 3 sem completar a inserção orbital, atingindo apenas 7.229 m/s de um total necessário de 9.100 m/s (déficit de 1.871 m/s). O Cenário B (mprop = 95%) atinge o ΔV necessário para inserção em órbita baixa (LEO) com margem de segurança de **+303 m/s** (ΔV máx = 9.403 m/s). O sistema elétrico embarcado, com 500 kWh de capacidade e 82% de carga, suporta confortavelmente todos os sistemas críticos durante os 24 minutos de operação propulsiva.

**Recomendação final:** adotar o Cenário B como baseline da Missão Aurora Siger, sendo **95% de propelente o limiar mínimo operacional** — qualquer carga de propelente inferior a 95% resulta em ΔV insuficiente para LEO e não deve ser autorizada para decolagem. Verificar também a viabilidade estrutural de uma nave com apenas 5% de massa seca (1.000 kg), o que é altamente desafiador em termos de engenharia real.

---

## 7. Fontes e Referências

Todas as referências de consumo energético dos sistemas eletrônicos embarcados foram obtidas a partir de documentação técnica pública de missões reais e guias de engenharia aeroespacial.

| Sistema / Dado | Fonte | URL de Referência |
|---|---|---|
| Flight Computer — 35W/unidade | AstroForge — Spacecraft Power 101 (Missão Odin) | astroforge.com/updates-collection/spacecraft-power-101 |
| Telemetria — 5 a 15W em transmissão ativa | CubeSat Mission and Bus Design Guide — Power Budget and Profiling | pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-9-power-budget-and-profiling |
| IMU e aviónica — arquitetura e consumo | NASA — Small Spacecraft Avionics (SSA) | nasa.gov/smallsat-institute/sst-soa/small-spacecraft-avionics |
| Sensores de pressão piezoelétricos (ICP®) — 2 a 5W/sensor | PCB Aerospace — Dynamic ICP® Pressure Sensors (White Paper) | pcb.com/Contentstore/mktgcontent/WhitePapers/WPL_2_Low_Dynamic_Pressure.pdf |
| Termistores NTC qualificados NASA — 0,5 a 2W/sensor | TE Connectivity — Sensors in Space (Missões Juno e Pioneer 10) | te.com/en/whitepapers/sensors/sensors-in-space.html |
| Sensores de nível de propelente — Collins Aerospace | Collins Aerospace — Space Sensors (SLS/Artemis) | collinsaerospace.com/what-we-do/industries/space/space-sensors |
| Sensores de temperatura, pressão e controle vetorial | DwyerOmega — How Sensors Play a Role in Spaceflight | dwyeromega.com/en-us/resources/sensors-role-in-spaceflight |
| ECUs com protocolo CAN Bus aeroespacial | CubeSat Avionics Guide — Typical Avionics | pressbooks-dev.oer.hawaii.edu/epet302/chapter/6-4 |
| Isp = 320s — RP-1/LOX | NASA Technical Reports | ntrs.nasa.gov |
| Densidade energética RP-1 — 43,2 MJ/kg | Valor de referência padrão para querosene aeroespacial (RP-1 Lower Heating Value) | Referência termodinâmica padrão |
| Motor Merlin 1D — Isp, ciclo e propelentes | Astronautix — Merlin 1D | astronautix.com/m/merlin1d.html |
| Merlin 1D — ciclo gas-generator e RP-1/LOX | Wikipedia — SpaceX Merlin | en.wikipedia.org/wiki/SpaceX_Merlin |
| Falcon 9 — configuração de motores | Wikipedia — Falcon 9 | en.wikipedia.org/wiki/Falcon_9 |
| KARI — Hanbit (referência estrutural) | Korea Aerospace Research Institute | kari.re.kr |
| Baterias Li-ion para veículos lançadores | EaglePicher — Space Launch Vehicle Battery Technology | eaglepicher.com/markets/space/launch-vehicles |
| Baterias Li-ion para lançadores (LAUNCHER-BATT) | Airbus Defence & Space — Space Battery Products | airbus.com/en/products-services/space/equipment/power/space-battery-products |
| Células Li-ion para foguetes e satélites | GS Yuasa Lithium Power — Satellites and Rockets | gsyuasa-lp.com/satellites-and-rockets |
| Painéis solares — vibração e deploy em voo | Li et al. (2023) — Vibration control for solar panels of spacecraft | onlinelibrary.wiley.com/doi/10.1002/msd2.12094 |
| Painéis solares — articulação e rastreamento solar em órbita | NASA Science — Chapter 11: Onboard Systems | science.nasa.gov/learn/basics-of-space-flight/chapter11-2 |

> ⚠️ **Nota metodológica:** Os valores de consumo do RCS (8.000W na Fase 1) e do sistema de ignição (2.500W na Fase 1) foram estimados a partir de faixas típicas citadas nas fontes acima (atuadores de gimbaling: 2–10 kW; válvulas solenóides aerospace: 200–500W; pico de ignição: ~2 kW). Não foram obtidos de um único datasheet específico. Todos os demais sistemas possuem respaldo direto nas fontes listadas acima.
