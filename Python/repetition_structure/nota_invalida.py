"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido econtinue pedindo até que o usuário informe um valor válido.
"""

while True:
    nota = float(input('\nInforme uma nota: ').replace(',', '.'))
    if nota < 0 or nota > 10:
        print('Nota inválida!')
        continue
    else:
        print(nota)
        break
