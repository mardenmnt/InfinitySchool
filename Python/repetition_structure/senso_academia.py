"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos
clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser
dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser
informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes
"""

mais_alto = 0
cod_mais_alto = 0
mais_baixo = 999
cod_mais_baixo = 0
mais_gordo = 0
cod_mais_gordo = 0
mais_magro = 999
cod_mais_magro = 0

total_peso = 0
total_altura = 0
cont = 0

while True:
    cod = int(input('\nInforme seu código: '))
    if cod == 0:
        break

    altura = float(input('Informe sua altura: ').replace(',', '.'))
    peso = float(input('Informe seu peso: ').replace(',', '.'))
    cont += 1

    if altura < mais_baixo:
        mais_baixo = altura
        cod_mais_baixo = cod
    if altura > mais_alto:
        mais_alto = altura
        cod_mais_alto = cod
    if peso < mais_magro:
        mais_magro = peso
        cod_mais_magro = cod
    if peso > mais_gordo:
        mais_gordo = peso
        cod_mais_gordo = cod

    total_peso += peso
    total_altura += altura

media_altura = total_altura / cont
media_peso = total_peso / cont

print('-'*30)
print('     Resultado final')
print('-'*30)
print(f'\nCliente {cod_mais_gordo} - mais gordo {mais_gordo} Kg')
print(f'Cliente {cod_mais_magro} - mais magro {mais_magro} Kg')
print(f'Cliente {cod_mais_alto} - mais alto {mais_alto} cm')
print(f'Cliente {cod_mais_baixo} - mais baixo {mais_baixo} cm')

print(f'\nPeso médio dos clientes - {media_peso:.2f} Kg')
print(f'Altura média dos clientes - {media_altura:.2f} cm')
