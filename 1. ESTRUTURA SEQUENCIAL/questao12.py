"""
12. Tendo como dados de entrada a altura de uma pessoa,
    construa um algoritmo que calcule seu peso ideal, 
    usando a seguinte fórmula: (72.7*altura) - 58
"""

print("[PESO IDEAL]")

altura = float(input("Qual sua altura? "))

peso_ideal = (72.7 * altura) - 58

print(f"> Seu peso ideal é: {peso_ideal:.2f}")
