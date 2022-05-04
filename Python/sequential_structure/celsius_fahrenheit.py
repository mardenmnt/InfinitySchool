"""
Crie programa que converta temperatura em Celsius para Fahrenheit
"""

celsius = int(input('\nInforme a temperatura em Celsius: '))

# cálculo para conversão
fahrenheit = ((celsius / 5) * 9) + 32

print(f'{celsius}º C equivale a {fahrenheit:.2f}º F')
