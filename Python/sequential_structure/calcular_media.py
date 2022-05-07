"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média
"""

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

print(f'A média das notas foi: {media:.2f}')
