"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1) o produto do dobro do primeiro com metade do segundo.
2) a soma do triplo do primeiro com o terceiro.
3) o terceiro elevado ao cubo.
"""

int1 = int(input('\nInforme um número inteiro: '))
int2 = int(input('Agora informe outro número inteiro: '))
real = float(input('Informe um número real: ').replace(',', '.'))

print(f'O produto do dobro do primeiro com metade do segundo é: {(int1 * 2) * (int2 / 2)}')
print('A soma do triplo do primeiro com o terceiro é: {}'.format((3 * int1) + real))
print('O terceiro elevado ao cubo é: {:.2f}'.format(real ** 3))
