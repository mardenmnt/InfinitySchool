from carro import Carro

if __name__ == '__main__':
    consumo = float(input('\nInforme o consumo do carro:'))

    carro = Carro(consumo)

    while True:
        print('\n[1] Andar\n'
              '[2] Obter gasolina\n'
              '[3] Adicionar Gasolina\n'
              '[4] Sair')
        menu = input()

        if menu == '1':
            distancia = float(input('Informe a distância em Km que deseja percorrer: '))
            print(carro.andar(distancia))
        elif menu == '2':
            print(carro.obter_gasolina)
        elif menu == '3':
            litros = float(input('Quantos litros deseja abastecer? '))
            print(carro.adicionar_gasolina(litros))
        elif menu == '4':
            print('Encerrando sistema...')
            break
        else:
            print('\nOpção inválida! Tente novamente')
            continue
