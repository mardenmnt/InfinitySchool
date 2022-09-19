"""
A NASA (Agência Espacial dos Estados Unidos) mantém um registro de todos os asteroides e suas distâncias relativas à Terra.
Você foi convidado para escrever um programa que leia o nome do asteroide e uma lista das suas últimas 5 distâncias da Terra.
Armazene os dados em um dicionário, onde a chave é o nome do asteroide. Exiba no final a distância média de todos os
asteroides registrados
"""

nomes = []
dicionario = {}
soma_distancias = []
media_individual = []
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

for soma in soma_distancias:
    media_individual.append(int(soma) / 5)

print(f"\nQuantidade de asteróides detectados: {len(nomes)}\n")
print("*"*30)
print("  Distância média indivisual")
print("*"*30)

for i in range(len(nomes)):
    print(f"{nomes[i]} teve distância média: {media_individual[i]}")

print("\n")
print("*"*30)
print("     Distância média geral")
print("*"*30)
print(f"Soma total das distâncias: {sum(soma_distancias)}")
print(f'Distância média de todos asteróides: {sum(soma_distancias)/len(nomes)}')
# print(f'Soma distância total / QTD distâncias: {sum(soma_distancias)/len(dist)}')
