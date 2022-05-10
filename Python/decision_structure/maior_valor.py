"""
Crie um programa que leia 2 numeros e imprima o maior
"""

num1 = float(input('\nInforme 1º número: ').replace(',', '.'))
num2 = float(input('Informe 2º número: ').replace(',', '.'))

# compara os valores
if num1 > num2:
    print('O maior número é', num1)
elif num2 > num1:
    print('O maior número é', num2)
else:
    print('Os números são iguais')
