"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
"""

from cmath import pi


raio = float(input('Informe o raio: '))

area = pi * (raio**2)

print(f'A área do círculo com raio {raio} vale: {area:.2f}')
