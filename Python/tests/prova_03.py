"""
Faça um programa que leia diversos números até o usuário informar que deseja parar.
Depois disso, informe a soma e a média dos números.
"""

cont = 1
soma = 0
while True:
    num = int(input(f'\nInforme o {cont}º número: '))
    soma += num
    continua = input('Deseja continuar? [S]im / [N]ão \n').upper().strip()[0]
    if continua == 'S':
        cont += 1
        continue
    else:
        print(f'\nA soma dos números foi: {soma}')
        print(f'A média dos números foi: {soma / cont:.2f}')
        break
