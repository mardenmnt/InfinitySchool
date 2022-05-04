"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
"""


fahrenheit = int(input('\nInforme a temperatura em Fahrenheit: '))

# cálculo para conversão
celsius = 5 * ((fahrenheit - 32) / 9)

print(f'{fahrenheit}º C equivale a {celsius:.2f}º F')