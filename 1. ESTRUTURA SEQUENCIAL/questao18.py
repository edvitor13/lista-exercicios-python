"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB)
    e a velocidade de um link de Internet (em Mbps), calcule e informe o 
    tempo aproximado de download do arquivo usando este link (em minutos). 
"""

print("[SUPER DOWNLOAD]")

tamanho = float(input("Informe o tamanho do arquivo (MB): "))
velocidade = float(input("Informe a velocidade de Download (Mbps): "))

# Download
tempo_minutos = int((tamanho / velocidade) / 60)
tempo_segundos = int((tamanho / velocidade) - (tempo_minutos * 60))

print(
    f"> O Download do arquivo de {tamanho:.2f}MB à " 
    f"{velocidade:.2f}Mbps demorará\n"
    f"  {tempo_minutos} minuto(s) e {tempo_segundos} segundo(s)"
)
