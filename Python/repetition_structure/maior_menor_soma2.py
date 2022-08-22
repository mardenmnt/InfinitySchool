"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

menor = 0
maior = 0

while True:
    num = int(input('\nInforme um número inteiro entre 0 e 1000: '))
    if num < 0 or num > 1000:
        print('Número inválido\n'
              'Tente novamente')
        continue
    elif num > maior:
        maior = num
    else:
        menor = num
    resp = input('\nDeseja continuar?\n'
                 '[S]im/[N]ão: ').upper()
    if resp == 'S':
        continue
    else:
        print(f'\nO menor valor foi: {menor}')
        print(f'O maior valor foi: {maior}')
        print(f'A soma é igual a: {menor + maior}')
        break