"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

valida = False

meses_31 = (1, 3, 5, 7, 8, 10, 12)
meses_30 = (4, 6, 9, 11)

if dia < 0 or dia > 31:
    print('Dia inválido!')
elif mes < 0 or mes > 12:
    print('Mês inválido')
elif ano < 0:
    print('Ano inválido!')
else:
    # Meses com 31 dias
    if mes in meses_31:
        if dia <= 31:
            valida = True
    # Meses com 30 dias
    elif mes in meses_30:
        if dia <= 30:
            valida = True
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29:
                valida = True
        elif dia <= 28:
            valida = True

    if valida:
        print('Data válida')
    else:
        print('Data inválida')
