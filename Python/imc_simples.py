"""
Crie um programa que calcule o IMC
"""

print('\nCalcule seu IMC')
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

# cálculo do IMC
imc = peso / (altura ** 2)

print('O seu IMC é:', round(imc, 3))
