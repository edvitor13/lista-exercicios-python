"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. Toda vez que ele traz 
um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
estado de São Paulo (50 quilos) deve pagar uma multa de 
R$ 4,00 por quilo excedente. João precisa que você faça um programa 
que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite 
e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas. 
"""

print("[PEIXARIA]")

peso = float(input("Digite o peso dos peixes: "))

PESO_LIMITE = 50
VALOR_MULTA = 4

# Utilizando Expressão Condicional (Operação Ternária)
excesso = (peso - PESO_LIMITE) if peso > PESO_LIMITE else 0

multa = excesso * VALOR_MULTA

if (excesso > 0):
    print(f"> Peso elevado, deverá pagar uma multa de " 
        f"R${multa:.2f} já que excedeu {excesso:.2f}kg")
else:
    print(f"> Peso adequado.")
