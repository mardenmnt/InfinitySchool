"""
Crie programa que leia receba as medidas dos lados de um triagulo e informe se é isosceles, escaleno ou equilatero
"""

base = float(input('Informe o valor da base do triângulo: '))
lado1 = float(input('Informe o valor do 1º lado: '))
lado2 = float(input('Informe o valor do 2º lado: '))

# comparação dos lados para saber o qual tipo de triângulo
if lado1 == lado2 and lado1 == base and lado2 == base:
    print('Esse é um triângulo Equilátero')
elif lado1 == lado2 or lado2 == base or lado1 == base:
    print('Esse é um triângulo Isósceles')
else:
    print('Esse é um triângulo Escaleno')
