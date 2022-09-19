
print('*' * 50)
print('        Seja bem-vindo(a) à Autêntica Moda')
print('*' * 50)

while True:
    valor = float(input('\nInforme o valor produto: '))
    if valor <= 0:
        print('Valor incorreto!\nTente novamente')
        continue
    else:
        print('Deseja comprar outro produto?')
        continua = input('[S]im / [N]ão\n').upper().strip()[0]

        saldo_compra = valor
        total = saldo_compra

        while continua == 'S':
            valor = float(input('Informe o valor produto: '))
            if valor <= 0:
                print('Valor incorreto!\nTente novamente\n')
                continue
            else:
                continua = input('[S]im / [N]ão\n').upper().strip()[0]
                saldo_compra = total + valor
                total = saldo_compra

        if total >= 200:
            print(f'\nO valor final de sua compra foi: R$ {total}')
            print(f'Parabéns!\nVocê ganhou frete grátis!')
        elif total < 200:
            print(f'\nO valor final de sua compra foi: R$ {total}')
            print('Que pena!\nO frete grátis está disponível apenas acima de R$ 200')
        break
