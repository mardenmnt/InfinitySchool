"""
Faça um Programa que receba e leia um vetor de 5 números inteiros e mostre-os
"""

num_inteiros = []

print('Informe 5 números inteiros:')

for i in range(5):
    num_inteiros.append(int(input(f'{i+1}º número: ')))

for j in num_inteiros:
    print(j, end=' ')
