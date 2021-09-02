"""
10. Faça um Programa que peça a temperatura em graus Celsius, 
    transforme e mostre em graus Fahrenheit.
"""

print("[CELSIUS] -> [FAHRENHEIT]")

celsius = float(input("Temperatura em Celsius: "))

fahrenheit = (celsius * (9 / 5)) + 32 # (°C . 9/5) + 32

print(f"> {celsius:.2f} °C = {fahrenheit:.2f} °F")
