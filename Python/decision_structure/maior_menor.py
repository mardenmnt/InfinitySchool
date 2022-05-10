"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = float(input('\nInforme o 1º número: ').replace(',', '.'))
num2 = float(input('Informe o 2º número: ').replace(',', '.'))
num3 = float(input('Informe o 3º número: ').replace(',', '.'))

if num1 < num2 < num3:
    print(f'O menor número é {num1} e o maior é {num3}')
elif num2 < num1 < num3:
    print(f'O menor número é {num2} e o maior é {num3}')
elif num2 < num3 < num1:
    print(f'O menor número é {num2} e o maior é {num1}')
elif num3 < num1 < num2:
    print(f'O menor número é {num3} e o maior é {num2}')
elif num3 < num2 < num1:
    print(f'O menor número é {num3} e o maior é {num1}')
elif num1 < num3 < num2:
    print(f'O menor número é {num1} e o maior é {num2}')
