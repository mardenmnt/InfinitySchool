"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta
e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).

As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""


cont = 1
notas = []
maior_nota = 0
menor_nota = 0

nome = input('\nInforme o nome do atleta: ')

while cont <= 7:
    if nome == '':
        exit()
    else:
        salto = float(input(f'Nota do {cont}º salto: '))
        notas.append(salto)
        cont += 1

# duplica lista de saltos para printar resultados
ordem = notas[:]
# armazenando maior e menos saltos
maior_nota = max(notas)
menor_nota = min(notas)
# removendo o maior e menor saltos da lista
notas.remove(max(notas))
notas.remove(min(notas))
# somando os itens restantes da lista
soma = sum(notas[0:6])
# calculando média
media = soma / 5

print('-'*40)
print(f'Atleta: {nome}')
print(f'Nota: {ordem[0]} ')
print(f'Nota: {ordem[1]} ')
print(f'Nota: {ordem[2]} ')
print(f'Nota: {ordem[3]} ')
print(f'Nota: {ordem[4]} ')
print(f'Nota: {ordem[5]} ')
print(f'Nota: {ordem[6]} \n')

print('-'*15, 'Resultado Final', '-'*15)
print(f'\nAtleta: {nome}')
print(f'\nMelhor Nota: {maior_nota} m')
print(f'Pior Nota: {menor_nota} m')
print(f'\nMédia dos demais saltos: {media:.2f} m')
