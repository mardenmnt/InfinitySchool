"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida
"""

altura = []
idade = []

for i in range(5):
    print(f'{i+1}ª pessoa:')
    idade.append(int(input(f'Idade: ')))
    altura.append((float(input(f'Altura: ').replace(',', '.'))))

altura.reverse()
idade.reverse()

print(f'Alturas: {altura}')
print(f'Idades: {idade}')
