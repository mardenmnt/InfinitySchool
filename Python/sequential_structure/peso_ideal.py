"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7 * h) - 58
Para mulheres: (62.1 * h) - 44.7
"""

altura = float(input('\nInforme sua altura: ').replace(',', '.'))

ideal_h = (72.7 * altura) - 58
ideal_m = (62.1 * altura) - 44.7

print(f'O peso ideal para homens com {altura}m de altura é: {ideal_h:.2f}')
print(f'O peso ideal para mulheres com {altura}m de altura é: {ideal_m:.2f}')
