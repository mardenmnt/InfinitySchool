"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas | % de Juros sobre o valor inicial da dívida
1                           0
3                           10
6                           15
9                           20
12                          25

Exemplo de saída do programa:
Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela
R$ 1.000,00       0                 1                       R$  1.000,00
R$ 1.100,00       100               3                       R$    366,00
R$ 1.150,00       150               6                       R$    191,67
"""

while True:
    juros = 0
    divida = float(input('\nInforme o valor de sua dívida: '))

    print('\n1 parcela - 0% de juros\n'
          '3 parcelas- 10% de juros\n'
          '6 parcelas- 15% de juros\n'
          '9 parcelas- 20% de juros\n'
          '12 parcelas- 25% de juros\n')
    parcela = int(input('Escolha uma opção de parcelamento:'))

    if parcela not in [1, 3, 6, 9, 12]:
        print('Opção inválida!\nTente novamente')
        continue

    elif parcela == 0:
        juros = 0
    elif parcela == 3:
        juros = 0.10
    elif parcela == 6:
        juros = 0.15
    elif parcela == 9:
        juros = 0.20
    elif parcela == 12:
        juros = 0.25


    valor_juros = divida * juros
    total = divida + valor_juros
    valor_parcela = total / parcela


    print(f'Valor dívida  |  Valor dos juros  |  Quantidade de parcelas  |  Valor da parcela\n'
          f'R$ {divida}         R$ {valor_juros}               {parcela}                    R$ {valor_parcela:.2f}')
    break
