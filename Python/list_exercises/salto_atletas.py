"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.

A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""

cont = 1
saltos = []
maior_salto = 0
menor_salto = 0

nome = input('Informe o nome do atleta: ')

while cont <= 5:
    if nome == '':
        exit()
    else:
        salto = float(input(f'Distância alcançada com o {cont}º salto: '))
        saltos.append(salto)
        cont += 1

# duplica lista de saltos para printar resultados
ordem = saltos[:]
# armazenando maior e menos saltos
maior_salto = max(saltos)
menor_salto = min(saltos)
# removendo o maior e menor saltos da lista
saltos.remove(max(saltos))
saltos.remove(min(saltos))
# somando os itens restantes da lista
soma = sum(saltos[0:4])
# calculando média
media = soma / 3

print('-'*30)
print(f'Atleta: {nome}')
print(f'Primeiro Salto: {ordem[0]} m')
print(f'Segundo Salto: {ordem[1]} m')
print(f'Terceiro Salto: {ordem[2]} m')
print(f'Quarto Salto: {ordem[3]} m')
print(f'Quinto Salto: {ordem[4]} m')

print(f'\nMelhor Salto: {maior_salto} m')
print(f'Pior Salto: {menor_salto} m')

print(f'\nMédia dos demais saltos: {media:.2f} m')
