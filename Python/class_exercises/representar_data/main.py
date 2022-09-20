
from data import *

if __name__ == '__main__':
    while True:
        dia = int(input('Dia: ').strip())
        if dia <= 0 or dia > 31:
            print('Dia inválido! Tente novamente')
            continue
        mes = int(input('Mês: ').strip())
        if mes <= 0 or mes > 12:
            print('Mês inválido! Tente novamente')
            continue
        ano = int(input('Ano: ').strip())
        if ano <= 0:
            print('Ano inválido! Tente novamente')
            continue

        data = Data(dia, mes, ano)

        while True:
            print('\nEscolha uma das opções abaixo:\n'
                  '1 - Ver data\n'
                  '2 - Avançar dia\n'
                  '3 - Mudar data\n'
                  '4 - Sair')
            opcao = input()

            if opcao == '1':
                data.to_string()

            elif opcao == '2':
                data.avancar_dia(dia, mes, ano)

            elif opcao == '3':
                data.mudar_data()

            elif opcao == '4':
                exit()

            else:
                print('Opção inválida! Tente novamente')
                continue
