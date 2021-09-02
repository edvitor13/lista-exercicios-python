"""
15. Faça um Programa que pergunte quanto você ganha por hora e o 
    número de horas trabalhadas no mês. Calcule e mostre o total do 
    seu salário no referido mês, sabendo-se que são descontados 11% 
    para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
    faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. 
"""

print("[SALÁRIO: 2]")

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas trabalhadas no mês? "))

TAXA_IR = 0.11
TAXA_INSS = 0.08
TAXA_SINDICATO = 0.05

salario_bruto = ganho_hora * horas_mes

ir = salario_bruto * TAXA_IR
inss = salario_bruto * TAXA_INSS
sindicato = salario_bruto * TAXA_SINDICATO

descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos

print(
    f"\n+ Salário Bruto: R${salario_bruto:.2f}\n"
    f"- IR (11%): R${ir:.2f}\n"
    f"- INSS (8%): R${inss:.2f}\n"
    f"- Sindicato (5%): R${sindicato:.2f}\n"
    f"= Salário Liquido: R${salario_liquido:.2f}"
)
