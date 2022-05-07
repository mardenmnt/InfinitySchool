"""
Faça um Programa que receba um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

inteiros = []
quadrados = []

for i in range(10):
    inteiros.append(int(input(f'Informe o {i+1}º número inteiro: ')))

for j in inteiros:
    quadrados.append(j**2)

soma = sum(quadrados)

print(f'\nNúmeros informados: {inteiros}')
print(f'Quadrado dos números: {quadrados}')
print(f'Soma dos quadrados: {soma}')
