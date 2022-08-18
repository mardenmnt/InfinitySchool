"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

# horizontal
cont = 0

while cont < 20:
    cont += 1
    print(cont)

# vertical
cont = 0

while cont < 20:
    cont += 1
    print(f'{cont}', end=' ')
