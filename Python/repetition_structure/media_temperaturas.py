"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que
leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""

while True:
    print('-'*40)
    print(' Departamento Estadual de Meteorologia')
    print('-' * 40)
    cont = 1
    soma = 0
    maior_temp = 0
    menor_temp = 999

    while True:
        temp = float(input(f'Informe a {cont}ª temperatura: '))
        soma += temp
        if temp < menor_temp:
            menor_temp = temp
        if temp > maior_temp:
            maior_temp = temp
        parar = input('\nDeseja continuar? [S]im/[N]ão\n').upper().strip()[0]
        if parar == 'S':
            cont += 1
            continue
        else:
            break
    media = soma / cont
    print(f'A menor temperatura {menor_temp}')
    print(f'A maior temperatura {maior_temp}')
    print(f'A média de todas temperaturas foi {media:.2f}')
    break

