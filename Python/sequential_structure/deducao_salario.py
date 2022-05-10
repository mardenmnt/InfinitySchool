"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

1) salário bruto.
2) quanto pagou ao INSS.
3) quanto pagou ao sindicato.
4) o salário líquido.
5) calcule os descontos e o salário líquido, conforme a tabela abaixo

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

sal_hora = float(input('\nInforme quanto ganha por hora: ').replace(',', '.'))
horas = float(input('Informe as horas trabalhadas: ').replace(',', '.'))

# cálculo salário bruto
sal_bruto = sal_hora * horas

# cálculo das taxas/impostos
taxa_ir = sal_bruto * 0.11
taxa_inss = (sal_bruto - taxa_ir) * 0.08
taxa_sindi = (sal_bruto - taxa_inss - taxa_ir) * 0.05

# soma de todos descontos
descontos = taxa_sindi + taxa_inss + taxa_sindi

# cálculo do saário líquido
sal_liqui = sal_bruto - descontos

print(f'+ Salário Bruto: {sal_bruto:.2f} reais')
print(f'- IR: {taxa_ir:.2f} reais')
print(f'- INSS: {taxa_inss:.2f} reais')
print(f'- Sindicato: {taxa_sindi:.2f} reais')
print(f'= Salário Líquido: {sal_liqui:.2f} reais')
