"""
Desenvolva um algoritmo que solicite o preço de três produtos e informe qual
produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato
"""

produto1 = float(input('Informe o valor do 1º produto: '))
produto2 = float(input('Informe o valor do 2º produto: '))
produto3 = float(input('Informe o valor do 3º produto: '))

# comparação do valor dos 3 produtos
if produto1 < produto2 and produto1 < produto3:
    print('O primeiro produto é mais barato que os outros')
elif produto2 < produto1 and produto2 < produto3:
    print('O segundo produto é mais barato que os outros')
elif produto3 < produto1 and produto3 < produto2:
    print('O terceiro produto é mais barato que os outros')

# criando uma correção para a possibilidade de 2 ou 3 produtos com preços iguais
elif produto1 == produto2 < produto3:
    print('Os produtos 1 e 2 têm valores iguais e são mais baratos que produto 3')
elif produto1 == produto3 < produto2:
    print('Os produtos 1 e 3 têm valores iguais e são mais baratos que produto 2')
elif produto2 == produto3 < produto1:
    print('Os produtos 2 e 3 têm valores iguais e são mais baratos que produto 1')
elif produto1 == produto2 == produto3:
    print('Os valores dos produtos são iguais')
