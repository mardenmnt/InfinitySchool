"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0
"""

lista_notas = []
notas_aluno = []

print('Notas dos alunos:')
for i in range(10):
    soma = 0
    notas_aluno = []
    print(f'\nAluno {i+1}')
    for j in range(4):
        notas_aluno.append(float(input(f'Nota {j+1} - ')))
        soma += notas_aluno[j]
    media = soma / 4
    lista_notas.append(media)

cont = 0
for k in lista_notas:
    if k >= 7:
        cont += 1
print(f'Total de alunos com média igual ou acima de 7: {cont}')
