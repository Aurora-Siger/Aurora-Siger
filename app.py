import time

# INPUTS
temp_interna      = float(input("Temperatura interna (-10 a 40°C): "))
temp_externa      = float(input("Temperatura externa (-5 a 45°C): "))
nivel_energia     = float(input("Nível de energia (% mínimo 70): "))
nivel_combustivel = float(input("Nível de combustível RP-1 (% mínimo 80): "))
nivel_oxidante    = float(input("Nível de oxidante LOX (% mínimo 80): "))
pressao_tanque    = float(input("Pressão do tanque (2.5 a 4.5 bar): "))
integridade       = int(input("Integridade estrutural (1 = OK, 0 = ERRO): "))

# CÁLCULOS
gradiente_termico = abs(temp_interna - temp_externa)
razao_mistura     = nivel_oxidante / nivel_combustivel 

print("\n[ Analisando sistema... ]\n")
time.sleep(0.5)

# VERIFICAÇÕES
resultados = []

if not (-10 <= temp_interna <= 40):
    resultados.append(("Temperatura interna", False, f"Fora do limite ({temp_interna}°C). Esperado: -10°C a 40°C."))
else:
    resultados.append(("Temperatura interna", True, None))

if not (-5 <= temp_externa <= 45):
    resultados.append(("Temperatura externa", False, f"Fora do limite ({temp_externa}°C). Esperado: -5°C a 45°C."))
else:
    resultados.append(("Temperatura externa", True, None))

if not (gradiente_termico <= 40):
    resultados.append(("Gradiente térmico", False, f"Gradiente excessivo ({gradiente_termico:.1f}°C). Máx: 40°C."))
else:
    resultados.append(("Gradiente térmico", True, None))

if not (nivel_energia >= 70):
    resultados.append(("Nível de energia", False, f"Energia insuficiente ({nivel_energia:.1f}%). Mín: 70%."))
else:
    resultados.append(("Nível de energia", True, None))

if not (nivel_combustivel >= 80):
    resultados.append(("Nível de combustível (RP-1)", False, f"Combustível insuficiente ({nivel_combustivel:.1f}%). Mín: 80%."))
else:
    resultados.append(("Nível de combustível (RP-1)", True, None))

if not (nivel_oxidante >= 80):
    resultados.append(("Nível de oxidante (LOX)", False, f"Oxidante insuficiente ({nivel_oxidante:.1f}%). Mín: 80%."))
else:
    resultados.append(("Nível de oxidante (LOX)", True, None))

if not (1.8 <= razao_mistura <= 2.2):
    resultados.append(("Razão de mistura LOX:RP-1", False, f"Proporção fora do limite ({razao_mistura:.2f}). Esperado: 1.8 a 2.2."))
else:
    resultados.append(("Razão de mistura LOX:RP-1", True, None))

if not (2.5 <= pressao_tanque <= 4.5):
    resultados.append(("Pressão do tanque", False, f"Pressão fora do intervalo ({pressao_tanque:.2f} bar). Esperado: 2.5–4.5 bar."))
else:
    resultados.append(("Pressão do tanque", True, None))

if not (integridade == 1):
    resultados.append(("Integridade estrutural", False, "Falha estrutural detectada."))
else:
    resultados.append(("Integridade estrutural", True, None))

status_modulos = all(passou for _, passou, _ in resultados)
resultados.append(("Status dos módulos", status_modulos, "Módulos com falha detectada."))

for nome, passou, erro in resultados:
    if not passou:
        print(f"  >> {nome}: FALHA")
        print(f"     {erro}")
        print("\n❌ DECOLAGEM ABORTADA")
        break
    print(f"  >> {nome}: OK")
    time.sleep(0.7)
else:
    print("\n✅ PRONTO PARA DECOLAR")
