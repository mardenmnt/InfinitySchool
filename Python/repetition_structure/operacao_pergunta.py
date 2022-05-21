"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
while True:
    num1 = float(input('Informe o 1º número: ').replace(',', '.'))
    num2 = float(input('Informe o 2º número: ').replace(',', '.'))

    print('Operaçõas disponíveis: ')
    print('[S] - Soma\n'
          '[B] - Subtração\n'
          '[M] - Multiplicação\n'
          '[D] - Divisão\n')
    operacao = input('Qual operação deseja realizar? ').upper()

    if operacao == 'S':
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
        print(f'{soma} é um número: ')
        if soma < 0:
            print('negativo')
        elif soma == 0:
            print('Neutro')
        else:
            print('positivo')
        if soma % 2 == 0:
            print('par')
        else:
            print('ímpar')
        if soma % 1 == 0:
            print('inteiro')
        else:
            print('decimal')
        break


    elif operacao == 'B':
        diferenca = num1 - num2
        print(f'{num1} - {num2} = {diferenca}')
        print(f'{diferenca} é um número: ')
        if diferenca < 0:
            print('negativo')
        elif diferenca == 0:
            print('Neutro')
        else:
            print('positivo')
        if diferenca % 2 == 0:
            print('par')
        else:
            print('ímpar')
        if diferenca % 1 == 0:
            print('inteiro')
        else:
            print('decimal')
        break

    elif operacao == 'M':
        multiplicacao = num1 * num2
        print(f'{num1} * {num2} = {multiplicacao}')
        print(f'{multiplicacao} é um número: ')
        if multiplicacao < 0:
            print('negativo')
        elif multiplicacao == 0:
            print('Neutro')
        else:
            print('positivo')
        if multiplicacao % 2 == 0:
            print('par')
        else:
            print('ímpar')
        if multiplicacao % 1 == 0:
            print('inteiro')
        else:
            print('decimal')
        break

    elif operacao == 'D':
        divisao = num1 / num2
        print(f'{num1} / {num2} = {divisao}')
        print(f'{divisao} é um número: ')
        if divisao < 0:
            print('negativo')
        elif divisao == 0:
            print('Neutro')
        else:
            print('positivo')
        if divisao % 2 == 0:
            print('par')
        else:
            print('ímpar')
        if divisao % 1 == 0:
            print('inteiro')
        else:
            print('decimal')
        break

    else:
        print('\nOpção inválida! Tente novamente')
        continue
