"""
A NASA (Agência Espacial dos Estados Unidos) mantém um registro de todos os asteroides e suas distâncias relativas à Terra.
Você foi convidado para escrever um programa que leia o nome do asteroide e uma lista das suas últimas 5 distâncias da Terra.
Armazene os dados em um dicionário, onde a chave é o nome do asteroide. Exiba no final a distância média de todos os
asteroides registrados
"""

nomes = []
dicionario = {}
soma_distancias = []
dist = []
soma = []

while True:
    distancias = []
    nomes.append(input('Informe o nome do asteroide: '))

    for i in range(5):
        num = int(input(f'Informe a {i + 1}ª distância: '))
        distancias.append(num)
        dist.append(num)

    for chave in nomes:
        dicionario[chave] = sum(distancias)

    novo = sorted(dicionario.items())
    soma_distancias.append(novo[0][1])

    resposta = input('\nDeseja continuar? ').upper().strip()[0]
    if resposta == 'S':
        continue
    else:
        break

print(f'\nSoma distância cada asteroide / QTD asteroides: {sum(soma_distancias)/len(nomes)}')
print(f'Soma distância total / QTD distâncias: {sum(soma_distancias)/len(dist)}')