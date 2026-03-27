# Aurora Siger - Sistema de Verificação de Pré-Decolagem

Sistema de telemetria e checklist automatizado para a Missão Aurora Siger. Realiza verificações dos parâmetros críticos da nave e decide se o sistema está apto para decolagem.

---

## Algoritmo de Verificação

```mermaid
flowchart TD
    A([INÍCIO]) --> B[Leitura dos inputs]
    B --> C{Temp. interna\n-10°C a 40°C?}
    C -- "Fora do limite.\nEsperado: -10°C a 40°C" --> Z
    C -- OK --> D{Temp. externa\n-5°C a 45°C?}
    D -- "Fora do limite.\nEsperado: -5°C a 45°C" --> Z
    D -- OK --> E[Calcular gradiente térmico\nabs·temp_interna - temp_externa·]
    E --> F{Gradiente\n≤ 40°C?}
    F -- "Gradiente excessivo.\nMáx: 40°C" --> Z
    F -- OK --> G{Nível de energia\n≥ 70%?}
    G -- "Energia insuficiente.\nMín: 70%" --> Z
    G -- OK --> H{Combustível RP-1\n≥ 80%?}
    H -- "Combustível insuficiente.\nMín: 80%" --> Z
    H -- OK --> I{Oxidante LOX\n≥ 80%?}
    I -- "Oxidante insuficiente.\nMín: 80%" --> Z
    I -- OK --> J{Pressão do tanque\n2.5 a 4.5 bar?}
    J -- "Pressão fora do intervalo.\nEsperado: 2.5–4.5 bar" --> Z
    J -- OK --> K{Integridade\nestrutural = 1?}
    K -- "Falha estrutural\ndetectada" --> Z
    K -- OK --> L{Status dos\nmódulos OK?}
    L -- "Módulos com\nfalha detectada" --> Z
    L -- OK --> Y

    Y([✅ PRONTO PARA DECOLAR])
    Z([❌ DECOLAGEM ABORTADA])
```

---

## Parâmetros Verificados

| Parâmetro | Tipo | Faixa Aceitável |
|---|---|---|
| Temperatura interna (eletrônicos) | Input | -10°C a 40°C |
| Temperatura externa (estrutura) | Input | -5°C a 45°C |
| Gradiente térmico | Calculado | ≤ 40°C |
| Nível de energia | Input | ≥ 70% |
| Nível de combustível RP-1 | Input | ≥ 80% |
| Nível de oxidante LOX | Input | ≥ 80% |
| Pressão do tanque | Input | 2.5 a 4.5 bar |
| Integridade estrutural | Input | 1 (OK) |
| Status dos módulos | Calculado | Todos OK |

---

## Como executar

**Requisitos:** Python 3.x

```bash
python app.py
```

O sistema solicitará cada parâmetro via terminal e exibirá o resultado da verificação linha a linha.
