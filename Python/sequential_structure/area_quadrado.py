"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
"""

lado = float(input('Informe o lado do quadrado: '))

# cálculo da área
area = lado * lado

dobro_area = area * 2

print(f'\nA área do quadrado é de {area}')
print(f'\nO dobro da área é {dobro_area}')
