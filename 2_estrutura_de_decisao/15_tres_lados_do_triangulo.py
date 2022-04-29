# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores 
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles 
# ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

import os 

os.system('cls' if os.name == 'nt' else 'clear')

lado_1 = float(input("Lado 1: "))
lado_2 = float(input("Lado 2: "))
lado_3 = float(input("Lado 3: "))

if lado_1 + lado_2 > lado_3 or lado_1 + lado_3 > lado_2 or lado_2 + lado_3 > lado_1:

  if lado_1 == lado_2 ==  lado_3:
    print("Triângulo Equilátero.")

  elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    print("Triângulo Isósceles.")

  elif lado_1 != lado_2 != lado_3:
    print("Triângulo Escaleno.")

else:
  print("Os lados informados não consegui fazer um triângulo.")
