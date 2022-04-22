"""
Faça um algoritmo que leia o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas
O índice de poluição aceitável varia de 0,05 até 0,25.
Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem as suas atividades,
se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem as suas atividades,
se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem as suas atividades.
"""

indice = float(input('Informe o índice de poluição: ').replace(',', '.'))

if 0.05 < indice <= 0.25:
    print('Índice de poluição normal')
elif 0.25 < indice <= 0.3:
    print('As indústrias do 1º grupo são intimadas a suspenderem suas atividades')
elif 0.3 < indice <= 0.4:
    print('As indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades')
elif 0.4 < indice <= 0.5:
    print('Todos os grupos devem ser notificados a paralisarem suas atividades')
else:
    print('Índice incorreto')


