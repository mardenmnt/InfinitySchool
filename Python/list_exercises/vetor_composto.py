"""
Faça um Programa que receba dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
"""

um = []
dois = []
tres = []

for i in range(10):
    um.append(input(f'Informe o {i+1}º elemento do vetor 1: '))

print('\n')

for j in range(10):
    dois.append(input(f'Informe o {j + 1}º elemento do vetor 2: '))

for k in range(10):
    tres.append(um[k])
    tres.append(dois[k])

print(f'Vetor 1: {um}')
print(f'Vetor 2: {dois}')
print(f'Vetor composto: {tres}')
