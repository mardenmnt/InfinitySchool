"""
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

total = 0
valor = 0

while True:
    cod = int(input('\nInforme o código do item: '))

    if cod not in [100, 101, 102, 103, 104, 105]:
        print('Código inválido!\nTente novamente')
        continue
    else:
        if cod == 100:
            item = 'Cachorro quente'
            valor = 1.20
        elif cod == 101:
            item = 'Bauru simples'
            valor = 1.30
        elif cod == 102:
            item = 'Bauru com ovo'
            valor = 1.50
        elif cod == 103:
            item = 'Hambúrguer'
            valor = 1.20
        elif cod == 104:
            item = 'Cheeseburguer'
            valor = 1.30
        elif cod == 105:
            item = 'Refrigerante'
            valor = 1.00

    qtd = int(input('Informe a quantidade do item: '))

    if qtd <= 0:
        print('Quantidade inválida!\nTente novamente')
        continue
    else:
        valor = valor * qtd
        total = total + valor

        pergunta = input('Deseja pedir algo mais? ').upper().strip()[0]

        if pergunta == 'S':
            continue
        else:
            print(f'\nTotal a pagar: R$ {total}')
            break
