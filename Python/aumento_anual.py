"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário.
"""


aumento = 0.015

salario = float(input('Informe o salário inicial: '))
ano_inicial = int(input('Informe o ano inicial: '))
ano_atual = int(input('Informe o ano final: '))

while ano_inicial < ano_atual:
    aumento *= 2
    salario = salario + (salario * aumento)
    ano_inicial += 1
    print(f'No ano de {ano_inicial} o salário foi: {salario:.2f}')



