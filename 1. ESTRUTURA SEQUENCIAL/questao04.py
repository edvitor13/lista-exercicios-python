"""
4. Faça um Programa que peça as 4 notas 
   bimestrais e mostre a média. 
"""

print("[BOLETIM ESCOLAR]")

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
nota4 = float(input("Informe a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"> Média: {media:.2f}")
