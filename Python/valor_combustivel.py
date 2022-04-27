"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

valor_gasolina = 2.50
valor_alcool = 1.90

litros = float(input('\nQuantos litros deseja abastecer? ').replace(',', '.'))

while litros <= 0:
    print('Valor inválido!')
    litros = float(input('\nQuantos litros deseja abastecer? ').replace(',', '.'))
else:
    print('[A] - Álcool\n'
          '[G] - Gasolina')
    escolha = input('Escolha um tipo de combustível: ').upper()

    while escolha != 'A' and escolha != 'G':
        print('Opção inválida!\n')
        print('[A] - Álcool\n'
              '[G] - Gasolina')
        escolha = input('Escolha um tipo de combustível: ').upper()
        print('Opção inválida!')

    else:
        if escolha == 'A':
            total = litros * valor_alcool
            print(f'Total a pagar é {total} reais')

        elif escolha == 'G':
            total = litros * valor_gasolina
            print(f'Total a pagar é {total} reais')
