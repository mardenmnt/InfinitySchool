from bomba import *

if __name__ == '__main__':

    print('-='*5, 'Posto Gonçalves', '-='*5)
    tipo_combustivel = input('Tipo de combustível: ')
    valor_litro = float(input('Valor/L: R$ '))
    qtd_combustivel = float(input(f'QTD de {tipo_combustivel}: '))

    bomba = BombaCombustivel(tipo_combustivel, valor_litro, qtd_combustivel)

    while True:
        print(f'\n------- {bomba.tipo_combustivel.upper()} -------')
        print(f'QTD disponível: {bomba.qtd_combustivel:.2f}L')
        print('-------------------------\n')
        print('Escolha uma opção:\n'
              '[1] Abastecer R$\n'
              '[2] Abastecer litros\n'
              '[3] Alterar valor por litro\n'
              '[4] Alterar tipo combustível\n'
              '[5] Alterar QTD combustível\n'
              '[6] Sair')
        menu = input()

        if menu == '1':
            valor = float(input('Informe o valor que deseja abastecer: R$ '))
            print(bomba.abastecer_valor(valor))
        elif menu == '2':
            litros = float(input('Informe QTD de litros que deseja abastecer: '))
            print(bomba.abastecer_litro(litros))
        elif menu == '3':
            valor = float(input(f'Informe um novo valor por litro para {tipo_combustivel} R$'))
            print(bomba.alterar_valor_litro(valor))
        elif menu == '4':
            tipo = input('Informe o novo tipo de combustível: ')
            print(bomba.alterar_tipo_combustivel(tipo))
        elif menu == '5':
            qtd = input(f'Informe a nova QTD de {tipo_combustivel}: ')
            print(bomba.alterar_qtd_combustivel(qtd))
        elif menu == '6':
            print('Encerrando sistema...')
            break
        else:
            print('Opção inválida!')
            continue
