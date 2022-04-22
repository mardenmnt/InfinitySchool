"""
Crie um programa que leia o nome de 2 times, o número de gols marcados na partida (para cada time).
E escreva o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE
"""

time1 = input('\nInforme o nome do time 1: ')
time2 = input('Informe o nome do time 2: ')

gols1 = int(input(f'\nInforme os gols do time {time1}: '))
gols2 = int(input(f'Informe os gols do time {time2}: '))

if gols1 > gols2:
    print(f'\nO time {time1} venceu!')
elif gols2 > gols1:
    print(f'\nO time', time2, 'venceu!\n')
else:
    print(time1, 'empatou com', time2)
