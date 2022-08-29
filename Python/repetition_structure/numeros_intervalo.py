"""
Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo compreendido por eles.
"""


while True:
    num1 = int(input(f'\nDigite 1º numero inteiro: '))
    num2 = int(input(f'Digite 2º numero inteiro: '))
    if num1 < 0 or num2 < 0:
        print('Número(s) inválido(s)\n'
              'Tente novamente')
        continue
    elif num1 == num2:
        print('Os números são iguais!\n'
              'Tente novamente')
        continue

    while num1 < num2:
        print(num1)
        num1 += 1

    while num2 < num1:
        print(num2)
        num2 += 1
    break
