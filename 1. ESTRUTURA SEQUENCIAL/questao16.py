"""
16. Faça um programa para uma loja de tintas. O programa deverá 
    pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 3 
    metros quadrados e que a tinta é vendida em latas de 18 litros, 
    que custam R$ 80,00. Informe ao usuário a quantidades de latas 
    de tinta a serem compradas e o preço total. 
"""

import math

print("[LOJA DE TINTAS]")

area = float(input("Qual o tamanho da área que deseja pintar? "))

LATA_LITROS = 18
LATA_CUSTO = 80
LATA_RENDIMENTO = LATA_LITROS * 3

"""
math.ceil arredonda o valor para cima
já que não é possível comprar 0.05 latas por exemplo
"""
latas_quantidade = math.ceil(area / LATA_RENDIMENTO)
preco_total = latas_quantidade * LATA_CUSTO

print(
    f"> Para pintar {area}m² será necessário comprar {latas_quantidade:d} "
    f"lata(s) de tinta.\n"
    f"  Valor Total de R${preco_total:.2f}"
)
