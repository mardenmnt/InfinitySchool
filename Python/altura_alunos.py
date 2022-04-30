"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e
o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

mais_baixo = 9999
mais_alto = 0
num_mais_baixo = 0
num_mais_alto = 0

for i in range(1, 11):
    num = input(f'\nInforme o número do {i}º aluno: ')
    altura = int(input(f'Informe a altura do {i}º aluno em cm: '))

    if altura <= mais_baixo:
        mais_baixo = altura
        num_mais_baixo = num
    if altura >= mais_alto:
        mais_alto = altura
        num_mais_alto = num

print(f'\nAluno(a) com número {num_mais_baixo} é o(a) baixo(a) e tem: {mais_baixo} cm')
print(f'Aluno(a) com número {num_mais_alto} é o(a) alto(a) e tem: {mais_alto} cm')
