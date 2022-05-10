"""
Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto.
"""

ano = int(input('Informe um ano: ').replace(',', '.'))

# um ano é bissexto se for divisível por 4, 400, mas não é por 100
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
