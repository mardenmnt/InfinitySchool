"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota1 = float(input('\nInforme a 1ª nota: ').replace(',', '.'))
nota2 = float(input('Informe a 2ª nota: ').replace(',', '.'))

media = (nota1 + nota2) / 2

if (nota1 < 0 or nota2 < 0) or (nota1 > 10 or nota2 > 10):
    print('Nota inválida, por favor confira sua nota')

else:
    if 9 < media <= 10:
        conceito = 'A'
    elif 7.5 < media <= 9:
        conceito = 'B'
    elif 6 < media <= 7.5:
        conceito = 'C'
    elif 4 > media <= 6:
        conceito = 'D'
    else:   # 0 <= media <= 4
        conceito = 'E'

    if conceito in ('A', 'B', 'C'):
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'


    print(f'\nNota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Sua Média foi: {media:.2f}')
    print(f'Conceito: {conceito}')
    print(f'Resultado: {resultado}')
