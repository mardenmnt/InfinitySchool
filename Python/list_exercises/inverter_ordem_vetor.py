"""
Faça um Programa que receba e leia um vetor de 10 números reais e mostre-os na ordem inversa
"""

num_inteiros = []

print('Informe 10 números inteiros:')

for i in range(10):
    num_inteiros.append(int(input(f'{i+1}º número: ')))

num_inteiros.reverse()

for j in num_inteiros:
    print(j, end=' ')
