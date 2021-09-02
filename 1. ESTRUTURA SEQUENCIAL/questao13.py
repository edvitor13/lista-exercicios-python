"""
13. Tendo como dado de entrada a altura (h) de uma pessoa,
    construa um algoritmo que calcule seu peso ideal,
    utilizando as seguintes fórmulas:
      - Para homens: (72.7*h) - 58
      - Para mulheres: (62.1*h) - 44.7
"""

print("[PESO IDEAL: 2]")

altura = float(input("Qual a altura? "))

homem_peso_ideal = (72.7 * altura) - 58
mulher_peso_ideal = (62.1 * altura) - 44.7

print(f"> Peso ideal para Homem: {homem_peso_ideal:.2f}")
print(f"> Peso ideal para Mulher: {mulher_peso_ideal:.2f}")
