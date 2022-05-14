"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""


print('\nResponda as perguntas abaixo com [S] ou [N]:')

cont = 0

perg_1 = input('Telefonou para a vítima? ').upper()
while perg_1 != 'S' and perg_1 != 'N':
    print('Opção inválida!')
    print('\nPor favor digite [S] ou [N]:')
    perg_1 = input('Telefonou para a vítima? ').upper()
if perg_1 == 'S':
    cont += 1

perg_2 = input('\nEsteve no local do crime? ').upper()
while perg_2 != 'S' and perg_2 != 'N':
    print('Opção inválida!')
    print('\nPor favor digite [S] ou [N]:')
    perg_2 = input('Telefonou para a vítima? ').upper()
if perg_2 == 'S':
    cont += 1

perg_3 = input('\nMora perto da vítima? ').upper()
while perg_3 != 'S' and perg_3 != 'N':
    print('Opção inválida!')
    print('\nPor favor digite [S] ou [N]:')
    perg_3 = input('Telefonou para a vítima? ').upper()
if perg_3 == 'S':
    cont += 1

perg_4 = input('\nDevia para a vítima? ').upper()
while perg_4 != 'S' and perg_4 != 'N':
    print('Opção inválida!')
    print('\nPor favor digite [S] ou [N]:')
    perg_4 = input('Telefonou para a vítima? ').upper()
if perg_4 == 'S':
    cont += 1

perg_5 = input('\nJá trabalhou com a vítima? ').upper()
while perg_5 != 'S' and perg_5 != 'N':
    print('Opção inválida!')
    print('\nPor favor digite [S] ou [N]:')
    perg_5 = input('Telefonou para a vítima? ').upper()
if perg_5 == 'S':
    cont += 1

if cont == 2:
    print('Você é suspeito!')
elif 3 <= cont <= 4:
    print('Você é cúmplice!')
elif cont == 5:
    print('Você é o assassino!')
else:
    print('Você inocente!')
