# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
# seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

salario = float(input("Informe seu salário atual: R$"))

if salario <= 280:
  reajuste = salario * 0.20
  salario_novo = reajuste + salario
  print(f"Salário antes do reajuste: R${salario}")
  print("Aumento de 20%")
  print(f"Reajuste: {reajuste}")
  print(f"Salário com o reajuste fica de R${salario_novo}.")

elif salario > 280 and salario <= 700:
  reajuste = salario * 0.15
  salario_novo = reajuste + salario
  print(f"Salário antes do reajuste: R${salario}")
  print("Aumento de 15%")
  print(f"Reajuste: {reajuste}")
  print(f"Salário com o reajuste fica de R${salario_novo}.")

elif salario > 700 and salario <= 1500:
  reajuste = salario * 0.10
  salario_novo = reajuste + salario
  print(f"Salário antes do reajuste: R${salario}")
  print("Aumento de 10%")
  print(f"Reajuste: {reajuste}")
  print(f"Salário com o reajuste fica de R${salario_novo}.")

elif salario > 1500:
  reajuste = salario * 0.05
  salario_novo = reajuste + salario
  print(f"Salário antes do reajuste: R${salario}")
  print("Aumento de 5%")
  print(f"Reajuste: {reajuste}")
  print(f"Salário com o reajuste fica de R${salario_novo}.")
