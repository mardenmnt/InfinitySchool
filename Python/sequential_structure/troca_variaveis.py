"""
Crie duas variáveis, atribua valor a cada uma e troque os seus valores, usando somente variáveis
"""

from doctest import OutputChecker


A = 10
B = 20

# cria uma variável temporária para armazenar valor de B
temp = B
B = A
A = temp

# ou A, B = B, A

print('O valor de A é:', A)
print('O valor de B é:', B)
