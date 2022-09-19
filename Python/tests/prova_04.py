"""
Uma das soft skills mais importantes no mundo da programação é a de ser criativo. Pensar fora da caixa.
Propomos então um desafio: Existem várias possibilidades de montarmos nossos algoritmos,
sabendo disso, crie CINCO maneiras diferentes de mostrar OLÁ, MUNDO! em tela.
"""
# maneira 1

var = 'Olá, mundo!'
while True:
    print(var)
    break

# maneira 2

var = True
ola = 'Olá, mundo!'
if var:
    print(ola)

# maneira 3

var = 'Olá, mundo!'
for i in var:
    print(i, end='')


# maneira 4

def olamundo():
    print('\nOlá, mundo!')


olamundo()

# maneira 5

inverso = '!odnum ,álO'
print(inverso[::-1])
