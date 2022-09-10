"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

while True:
    user = input('\nInforme seu usuário: ')
    senha = input('Informe sua senha: ')
    if senha == user:
        print('Sua senha não pode ser seu nome!\n'
              'Tente novamente')
        continue
    else:
        print('Conta criada com sucesso!')
        break
