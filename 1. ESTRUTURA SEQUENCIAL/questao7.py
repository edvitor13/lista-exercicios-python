"""
7. Faça um Programa que calcule a área de um quadrado, 
   em seguida mostre o dobro desta área para o usuário. 
"""

print("[ÁREA DO QUADRADO x 2]")

lateral = float(input("Digite a medida de um lado do quadrado: "))

area = lateral ** 2 # l²

print("> Área em Dobro:", area * 2)
