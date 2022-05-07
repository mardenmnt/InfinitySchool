"""
Faça um Programa que receba 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores
"""

pares = []
impares = []
numeros = []

for i in range(20):
    numeros.append(int(input(f'Informe o {i+1}º número inteiro: ')))

    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'\nNúmeros: {numeros}')
print(f'Ímpares: {impares}')
print(f'Pares: {pares}')
