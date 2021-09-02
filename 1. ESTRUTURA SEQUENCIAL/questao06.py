"""
6. Faça um Programa que peça o raio de um círculo,
   calcule e mostre sua área.
"""

import math

print("[ÁREA DO CÍRCULO]")

raio = float(input("Digite o raio da circunferência: "))

area = math.pi * (raio ** 2) # π . r²

print("> Área:", area)
