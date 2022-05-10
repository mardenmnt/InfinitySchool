"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e
que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

sal_hora = float(input('\nInforme quanto ganha por hora: ').replace(',', '.'))
horas = float(input('Informe as horas trabalhadas no mês: ').replace(',', '.'))

sal_bruto = sal_hora * horas
sind = sal_bruto * 0.03
fgts = sal_bruto * 0.11

if sal_bruto <= 900:
    ir_taxa = 'ISENTO'
    ir_valor = 0
    sal_liquido = sal_bruto - sind
elif 900 < sal_bruto <= 1500:
    ir_taxa = '(5%)'
    ir_valor = sal_bruto * 0.05
    sal_liquido = sal_bruto - ir_valor - sind
elif 1500 < sal_bruto <= 2500:
    ir_taxa = '(10%)'
    ir_valor = sal_bruto * 0.10
    sal_liquido = sal_bruto - ir_valor - sind
else:
    ir_taxa = '(20%)'
    ir_valor = sal_bruto * 0.20
    sal_liquido = sal_bruto - ir_valor - sind

print(f'\nSalário Bruto: ({sal_hora} * {horas})----------: R$ {sal_bruto}')
print(f'(-) IR {ir_taxa}---------------------------: R$ {ir_valor}')
print(f'(-) Sindicato (3%)--------------------: R$ {sind}')
print(f'FGTS (11%)----------------------------: R$ {fgts:.2f}')
print(f'Total de descontos--------------------: R$ {round(sind+ir_valor, 2)}')
print(f'Salário Líquido-----------------------: R$ {sal_liquido:.2f}')
