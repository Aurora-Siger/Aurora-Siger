import time
import math

# INPUTS
temp_interna      = float(input("Temperatura interna (-10 a 40): "))
temp_externa      = float(input("Temperatura externa (-5 a 45): "))
nivel_energia     = float(input("Nível de energia (% mínimo 70): "))
nivel_combustivel = float(input("Nível de combustível (% mínimo 80): "))
pressao_tanque    = float(input("Pressão do tanque (2.5 a 4.5 bar): "))
autonomia         = float(input("Autonomia (mínimo 3 horas): "))
integridade       = int(input("Integridade estrutural (1 = OK, 0 = ERRO): "))
modulos_ok        = int(input("Todos os módulos estão OK? (1 = SIM, 0 = NÃO): "))

# CÁLCULO
gradiente = abs(temp_interna - temp_externa)

print("\n[ Analisando sistema... ]\n")
time.sleep(0.5)

# VERIFICAÇÕES
resultados = []

if not (-10 <= temp_interna <= 40):
    resultados.append(("Temperatura interna", False, f"Temperatura interna fora do limite permitido ({temp_interna}°C). Deve estar entre -10°C e 40°C."))
else:
    resultados.append(("Temperatura interna", True, None))

if not (-5 <= temp_externa <= 45):
    resultados.append(("Temperatura externa", False, f"Temperatura externa fora do limite permitido ({temp_externa}°C). Deve estar entre -5°C e 45°C."))
else:
    resultados.append(("Temperatura externa", True, None))

if not (gradiente <= 40):
    resultados.append(("Gradiente térmico", False, f"Gradiente térmico fora do limite permitido ({gradiente:.1f}°C). Deve estar entre -10°C e 40°C."))
else:
    resultados.append(("Gradiente térmico", True, None))


for nome, passou, erro in resultados:
    if not passou:
        print(f"  >> {nome}: FALHA")
        print(f"     {erro}")
        print("\n❌ SISTEMA NÃO APTO PARA DECOLAGEM")
        break
    print(f"  >> {nome}: OK")
    time.sleep(0.7)
else:
    print("\n✅ SISTEMA APTO PARA DECOLAGEM")
