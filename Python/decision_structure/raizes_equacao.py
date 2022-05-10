"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

1) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
o programa não deve fazer pedir os demais valores, sendo encerrado;
2) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
3) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
4) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math

a = float(input('Informe o coeficiente a: '))

if a == 0:
    print('Essa equação não é do segundo grau!')
else:
    b = float(input('Informe o coeficiente b: '))
    c = float(input('Informe o coeficiente c: '))
    delta = b ** 2 - (4 * a * c)

    if delta < 0:
        print('A equação não possui raízes reais!')
    elif delta == 0:
        raiz = -b / (2 * a)
        print('Delta = 0 , raiz =', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)   # (-b + raíz quadrada do delta) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Raizes: {raiz1:.2f} e {raiz2:.2f}')
