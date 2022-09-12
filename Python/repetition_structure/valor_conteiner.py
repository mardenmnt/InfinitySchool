"""
Uma empresa de exportação de Eletrodos vende contêineres com valores fixos por toneladas.
Um caminhão pode sair com várias toneladas e foi preciso desenvolver um sistema para calcular o valor mensal faturado.
Desenvolva este sistema que irá solicitar o valor fixo da tonelada no início do programa e peça para o usuário
quantas vezes forem necessárias a quantidade de toneladas que saiu (cada mês pode sair quantidade diferente).
Ao final, mostre o valor total faturado
"""

cont = 0
vezes = 1

valor = float(input('\nValor por tonelada: '))

while cont <= vezes:
    tonelada = float(input('\nInforme quantidade toneladas desse mês: '))
    print(f'Valor total da carga: R$ {valor * tonelada}')
    cont += 1
