"""
Crie programa que recebe um valor e informa se é positivo ou negativo
"""

num = float(input('\nInforme um número: '))

if num > 0:
    print('Esse número é positivo')
elif num < 0:
    print('Esse número é negativo')
else:
    print('O zero é um numero neutro')