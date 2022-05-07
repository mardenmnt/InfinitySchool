"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

numeros = []
soma = 0
multi = 1
for i in range(5):
    numeros.append(int(input(f'Informe o {i+1} número inteiro: ')))
    soma += numeros[i]
    multi *= numeros[i]

print(f'\nNumeros: {numeros}')
print(f'Soma dos numeros: {soma}')
print(f'Multiplicação dos números: {multi}')
