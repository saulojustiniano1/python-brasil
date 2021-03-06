# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular 
# a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

nota_1 = float(input("Informe sua 1ª nota: "))
nota_2 = float(input("Informe sua 2ª nota: "))
nota_3 = float(input("Informe sua 3ª nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7 and media < 10:
  print(f"Sua média foi de {media}.")
  print("Aprovado.")

elif media < 7:
  print(f"Sua média foi de {media}.")
  print("Reprovado.")

elif media == 10:
  print(f"Sua média foi de {media}.")
  print("Aprovado com Distinção.")
