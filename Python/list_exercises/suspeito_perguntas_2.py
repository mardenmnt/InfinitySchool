"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

respostas = []
cont = 0

for i in range(1):
    respostas.append(input('Telefonou para a vítima? [S/N]\n'))
    respostas.append(input('Esteve no local do crime? [S/N]\n'))
    respostas.append(input('Mora perto da vítima? [S/N]\n'))
    respostas.append(input('Devia para a vítima? [S/N]\n'))
    respostas.append(input('Já trabalhou com a vítima? [S/N]\n'))

for j in respostas:
    if j in ['s', 'S']:
        cont += 1

if cont == 2:
    print('\nSuspeito')
elif 3 <= cont <= 4:
    print('\nCúmplice')
elif cont == 5:
    print('\nAssassino')
else:
    print('\nInocente')
