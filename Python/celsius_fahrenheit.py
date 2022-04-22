"""
Crie programa que converta temperatura em Celsius para Fahrenheit
"""

celsius = int(input('\nInforme a temperatura em Celsius: '))

# cálculo para conversão
fahrenheit = ((celsius / 5) * 9) + 32

print(str(celsius)+'º', 'C equivale à', str(fahrenheit)+'º', 'F')
