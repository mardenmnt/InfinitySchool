"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
valor do desconto e valor a pagar.
"""
preco_bruto = 0

print('Tipos de carnes: ')
print('                   Até 5Kg               Acima de 5Kg')
print('[F] - Filé duplo ----- R$ 4,90/Kg ------------ R$ 5,80/Kg\n'
      '[A] - Alcatra -------- R$ 5,90/Kg ------------ R4 6,80/Kg\n'
      '[P] - Picanha -------- R$ 6,90/Kg ------------ R$ 7,80/Kg\n')

tipo_de_carne = input('Qual tipo de carne deseja? ').upper().strip()[0]
peso = float(input(f'Quantos Kg deseja? ').replace(',', '.'))

if peso > 5:
    preco_file = 5.80
    preco_alcatra = 6.80
    preco_picanha = 7.80
else:
    preco_file = 4.90
    preco_alcatra = 5.90
    preco_picanha = 6.90

# Define o preco bruto

if tipo_de_carne == 'F':
    preco_bruto = preco_file * peso
    tipo_de_carne = 'File Duplo'
elif tipo_de_carne == 'A':
    preco_bruto = preco_alcatra * peso
    tipo_de_carne = 'Alcatra'
elif tipo_de_carne == 'P':
    preco_bruto = preco_picanha * peso
    tipo_de_carne = 'Picanha'
else:
    print('Escolha errada')

cliente_hiper = (input('Tem cartao do Hipermercado? [s]im/[N]ao\n--> ')).upper().strip()[0]

desconto = preco_bruto * 0.05

if cliente_hiper == 'S':
    preco_final = preco_bruto - desconto
    ativo = 'Sim'
    desconto = desconto
else:
    preco_final = preco_bruto
    ativo = 'Não'
    desconto = 0


print('\n-------------------------- CUPOM FISCAL -------------------------------------')
print(f'* Carne.......................................................... {tipo_de_carne}')
print(f'* Quantidade..................................................... KG {peso:.2f}')
print(f'* Preço.......................................................... R$ {preco_bruto:.2f}')
print(f'* Cartao Tabajara................................................ R$ {ativo}')
print(f'* Desconto....................................................... R$ {desconto:.2f}')
print(f'* Total com desconto............................................. R$ {preco_final:.2f}')
print(f'------------------------------------------------------------------------------')
