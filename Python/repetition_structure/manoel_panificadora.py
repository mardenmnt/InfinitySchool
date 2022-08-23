"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela
de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""


print('-'*50)
print('     Lojas Quase Dois - Tabela de preços')
print('-'*50)


while True:
    pao = float(input('Informe o preço o pão: ').replace(',', '.'))
    if pao < 0:
        print('Valor incorreto, tente novamente')
        continue
    else:
        for i in range(1, 51):
            total = i * pao
            print(f'\t{i} - {total:.2f}')
    break
