"""
Faça um Programa que leia três números e mostre-os em ordem decrescente
"""

valor1 = float(input('\nInforme o 1º número: ').replace(',', '.'))
valor2 = float(input('Informe o 2º número: ').replace(',', '.'))
valor3 = float(input('Informe o 3º número: ').replace(',', '.'))

if valor1 < valor2 < valor3:
    print(f'Ordem decrescente dos números informados é: {valor3}, {valor2}, {valor1}')
elif valor1 < valor3 < valor2:
    print(f'Ordem decrescente dos números informados é: {valor2}, {valor3}, {valor1}')
elif valor3 < valor1 < valor2:
    print(f'Ordem decrescente dos números informados é: {valor2}, {valor1}, {valor3}')
elif valor2 < valor1 < valor3:
    print(f'Ordem decrescente dos números informados é: {valor3}, {valor1}, {valor2}')
elif valor2 < valor3 < valor1:
    print(f'Ordem decrescente dos números informados é: {valor1}, {valor3}, {valor2}')
elif valor3 < valor2 < valor1:
    print(f'Ordem decrescente dos números informados é: {valor1}, {valor2}, {valor3}')
