"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês
"""

valor_hora = float(input('Informe quanto ganha por hora: '))
horas = float(input('Informe as horas trabalhadas nesse mês: '))

salario = valor_hora * horas

print(f'O salário desse mês corresponde a R$ {salario}')
