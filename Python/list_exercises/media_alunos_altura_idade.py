"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos
"""


alturas = []
idades = []
altura_13 =[]
cont = 0

for i in range(5):
    altura = float(input(f'Informe a altura do(a) {i + 1}º aluno(a): '))
    alturas.append(altura)

    idade = int(input(f'Informe a idade do(a) {i + 1}º aluno(a): '))
    idades.append(idade)

    if idade > 13:
        altura_13.append(altura)

media_altura = sum(altura_13) / len(altura_13)      

for j in altura_13:
    if j < media_altura:
        cont += 1

print(f'\nExistem {cont} alunos(as) com altura abaixo da média {media_altura:.2f} m')
