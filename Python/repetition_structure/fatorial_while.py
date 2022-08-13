"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120
"""

num = int(input('Informe numero: '))
temp = num
fatorial = 1

while num >= 1:
    fatorial *= num
    num -= 1
print(f'O fatorial de {temp} é {fatorial}')
