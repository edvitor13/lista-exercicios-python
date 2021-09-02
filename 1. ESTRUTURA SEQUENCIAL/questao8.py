"""
8. Faça um Programa que pergunte quanto você ganha por hora e o 
   número de horas trabalhadas no mês. 
   Calcule e mostre o total do seu salário no referido mês.
"""

print("[SALÁRIO]")

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas trabalhadas no mês? "))

salario = ganho_hora * horas_mes

print(f"> Seu salário mensal é: {salario:.2f}")
