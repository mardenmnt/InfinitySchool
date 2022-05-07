"""
Faça um Programa que receba um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes
"""

caracteres = []
consoantes = 0

print('Informe os caracteres')

for i in range(10):
    caracteres.append((input('Caracter  ' + str(i + 1) + ':\n')))
    char = caracteres[i]
    if char not in 'aeiou':
        consoantes += 1

print(f'Total de consoantes: {consoantes}')
