"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

num = int(input('Informe um número inteiro para ser invertido: '))

invertido = str(num)[::-1]

print('\nNúmero:', num)
print('Número Invertido:', invertido)
