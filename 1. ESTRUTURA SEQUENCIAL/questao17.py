"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o 
    tamanho em metros quadrados da área a ser pintada. Considere que a 
    cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
    tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
    de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os 
    respectivos preços em 3 situações:
      1. comprar apenas latas de 18 litros;
      2. comprar apenas galões de 3,6 litros;
      3. misturar latas e galões, de forma que o desperdício de tinta 
        seja menor. Arredonde os valores para cima, 
        isto é, considere latas cheias. 
"""

import math

print("[LOJA DE TINTAS: 2]")

area = float(input("Qual o tamanho da área que deseja pintar? "))

# Informações Lata
LATA_LITROS = 18
LATA_CUSTO = 80
LATA_RENDIMENTO = LATA_LITROS * 6

# Informações Galão
GALAO_LITROS = 3.6
GALAO_CUSTO = 25
GALAO_RENDIMENTO = GALAO_LITROS * 6

# Calculando quantidades
# Situação 1
latas_quantidade_s1 = math.ceil(area / LATA_RENDIMENTO)
preco_total_s1 = latas_quantidade_s1 * LATA_CUSTO

# Situação 2
galoes_quantidade_s2 = math.ceil(area / GALAO_RENDIMENTO)
preco_total_s2 = galoes_quantidade_s2 * GALAO_CUSTO

# Situação 3
latas_quantidade_s3 = int(area / LATA_RENDIMENTO)

# Calculando quantidade de galões com base na área restante
_area_pintada = (latas_quantidade_s3 * LATA_RENDIMENTO)
_area_restante = (area - _area_pintada)
galoes_quantidade_s3 = math.ceil(_area_restante / GALAO_RENDIMENTO)

# Preço Total
_preco_total_latas = (latas_quantidade_s3 * LATA_CUSTO)
_preco_total_galoes = (galoes_quantidade_s3 * GALAO_CUSTO)
preco_total_s3 = _preco_total_latas + _preco_total_galoes

# Exibindo resultados
print()
print("> Custos Totais:")
print()
print(f"  Opções para pintar uma área {area}m²")
print()
print("  1. Comprando apenas latas de 18 litros")
print(f"     - QUANTIDADE: {latas_quantidade_s1} lata(s)")
print(f"     - VALOR TOTAL: R${preco_total_s1:.2f}")
print()
print("  2. Comprando apenas galões de 3,6 litros")
print(f"     - QUANTIDADE: {galoes_quantidade_s2} galão(ões)")
print(f"     - VALOR TOTAL: R${preco_total_s2:.2f}")
print()
print("  3. Comprando latas e galões")
print(
    f"     - QUANTIDADE: {latas_quantidade_s3} lata(s) "
    f"e {galoes_quantidade_s3} galão(ões)"
)
print(f"     - VALOR TOTAL: R${preco_total_s3:.2f}")
