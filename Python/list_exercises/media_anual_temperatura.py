"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )
"""


temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
soma = 0
acima_media = {}

for i in range(len(meses)):
    temperaturas.append(float(input(f'Informe a temperatura média de {meses[i]}: ')))
    soma += temperaturas[i]
media = soma / len(meses)

for j in range(len(meses)):
    if (temperaturas[j] > media):
        acima_media.update({meses[j] : temperaturas[j]})

print(f'Média anual das temperaturas: {media:.2f} ºC')
print(f'Meses com temperatura acima da média: {acima_media}')
