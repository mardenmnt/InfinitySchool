"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

— O total de votos para cada candidato;
— O total de votos nulos;
— O total de votos em branco;
— A percentagem de votos nulos sobre o total de votos;
— A percentagem de votos em branco sobre o total de votos.
— Para finalizar o conjunto de votos tem-se o valor zero.
"""

num1, num2, num3, num4, nulos, brancos = 0, 0, 0, 0, 0, 0
candidato1, candidato2, candidato3, candidato4 = '', '', '', ''
total_votos = 0

while True:
    print('\nEscolha a opção referente ao seu candidato:')
    print('1 - Francisco / 2 - Antônio / 3 - Carlinhos / 4 - Carluce\n'
          '5 - Nulo     / 6 - Branco  / 0 - Sair\n')
    voto = int(input())

    if voto == 0:
        break

    if voto not in [1, 2, 3, 4, 5, 6]:
        print('Voto inválido!\nTente novamente')
    elif voto == 1:
        num1 += 1
        candidato1 = 'Francisco'
    elif voto == 2:
        num2 += 1
        candidato2 = 'Antônio'
    elif voto == 3:
        num3 += 1
        candidato3 = 'Carlinhos'
    elif voto == 4:
        num4 += 1
        candidato4 = 'Carluce'
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1

    total_votos += 1

print('-'*30)
print(' Total de votos por canditato')
print('-'*30)
print(f'{candidato1} teve {num1} votos')
print(f'{candidato2} teve {num2} votos')
print(f'{candidato3} teve {num3} votos')
print(f'{candidato4} teve {num4} votos\n')
print('-'*30)
print('     Brancos e Nulos')
print('-'*30)
print(f'Total de votos em Branco {brancos}')
print(f'Total de votos em Nulos {nulos}')
print(f'Percentagem de votos nulos sobre o total: {(nulos / total_votos) * 100:.2f}%')
print(f'Percentagem de votos em branso sobre o total: {(brancos / total_votos) * 100:.2f}%')
