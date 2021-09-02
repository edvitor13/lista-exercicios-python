"""
9. Faça um Programa que peça a temperatura em graus Fahrenheit,
   transforme e mostre a temperatura em graus Celsius.
   C = 5 * ((F-32) / 9).
"""

print("[FAHRENHEIT] -> [CELSIUS]")

fahrenheit = float(input("Temperatura em Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print(f"> {fahrenheit:.2f} °F = {celsius:.2f} °C")
