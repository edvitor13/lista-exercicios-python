"""
11. Faça um Programa que peça 2 números inteiros e um número real.
    Calcule e mostre: 
      a) o produto do dobro do primeiro com metade do segundo.
      b) a soma do triplo do primeiro com o terceiro. 
      c) o terceiro elevado ao cubo.
"""

print("[CACULADOR]")

numero1 = int(input("Digite um Número Inteiro: "))
numero2 = int(input("Digite outro Número Inteiro: "))
numero3 = float(input("Digite um Número Real: "))

calculo_a = (numero1 * 2) * (numero2 / 2)
calculo_b = (numero1 * 3) + numero3
calculo_c = numero3 ** 3

print()
print("a) O produto do dobro do primeiro com metade do segundo:")
print(calculo_a)

print()
print("b) A soma do triplo do primeiro com o terceiro:")
print(calculo_b)

print()
print("c) O terceiro elevado ao cubo:")
print(calculo_c)
