"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e
o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um
"""


total = 0
cont = 1

qtd = int(input('\nInforme a quantidade de CDs de sua coleção: '))
while qtd < 0:
    print('Valor incorreto, tente novamente')
    qtd = int(input('\nInforme a quantidade de CDs de sua coleção: '))
    continue

while cont <= qtd:
    valor = float(input(f'Informe o valor do {cont}º Cd: '))
    if valor < 0:
        print('\nValor incorreto, tente novamente')
        continue
    else:
        total += valor
        cont += 1
media = total / qtd
print(f'\nO valor médio gasto nessa coleção foi de R$ {media:.2f}')

