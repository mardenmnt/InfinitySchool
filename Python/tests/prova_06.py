"""
Escreva uma função que recebe um determinado ano e retorne o século daquele ano.

Exemplo:
Entrada -> 1453
Saída   -> XV
"""
import math


def ano_seculo():

    while True:
        ano = int(input('\nInforme um ano: '))

        # separa a parte inteira da divisão
        seculo_decimal = int(math.ceil((ano / 100)))

        romanos_int = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        romanos = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        seculo_romano = []

        for i in range(len(romanos_int)):
            # divisão do seculo decimal com os romanos inteiros, para saber quais são divisores
            div = int(seculo_decimal / romanos_int[i])
            # adiciona o número romano na lista seculo_romano
            seculo_romano.append(romanos[i] * div)
            # decrementa seculo_decimal de acordo com seus divisores
            seculo_decimal = seculo_decimal - (romanos_int[i] * div)
            # juntar os valores da lista seculo_romano
        print('Século', ''.join(seculo_romano))

        pergunta = input('\nDeseja continuar? [S]im/[N]ão\n').upper().strip()[0]

        if pergunta == 'S':
            continue
        else:
            break


ano_seculo()
