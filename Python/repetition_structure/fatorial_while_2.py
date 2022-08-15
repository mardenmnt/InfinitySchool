"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120

Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16
"""

while True:
    num = int(input('\nInforme numero entre 0 e 16: '))
    if 0 < num < 16:
        fatorial = 1
        temp = num
        while num > 1:
            fatorial *= num
            num -= 1
        print(f'O fatorial de {temp} é {fatorial}')
        break
    else:
        print('Número incorreto\n'
              'Tente novamente')
        continue
