"""
Faça um Programa que receba 4 notas, mostre as notas e a média na tela
"""

notas = []
soma = 0

print('Informe as 4 notas:')

for i in range(4):
    notas.append(float(input(f'Informe a {i+1}ª nota: ')))
    soma += notas[i]

media = soma / 4
print('\n')
for j in notas:
    print(j , end=', ')
print(f'\nMédia das notas: {media}')
