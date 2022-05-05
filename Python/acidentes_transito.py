"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.

Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

cont = 000
maior_acidente = 0
menor_acidente = 999999
cod_maior_acidente = 0
cod_menor_acidente = 0
soma_veiculos = 0
soma_acidentes = 0
soma_menor_2000 = 0
cont_2000 = 0
media_acidentes_2000 = 0


while cont < 5:
    cod = input(f'\nInforme o código da {cont+1}ª cidade: ')
    num_veiculos = int(input(f'Informe o número de veículos de passeio da {cont+1}ª cidade: '))
    num_acidentes = int(input(f'Informe o número de acidentes de trânsito COM vítimas da {cont+1}ª cidade: '))

    if num_veiculos >= maior_acidente:
        maior_acidente = num_acidentes
        cod_maior_acidente = cod
    if num_acidentes <= menor_acidente:
        menor_acidente = num_acidentes
        cod_menor_acidente = cod

    if num_acidentes < 2000:
        soma_menor_2000 += num_acidentes
        cont_2000 += 1

    cont += 1

    soma_veiculos += num_veiculos
    soma_acidentes += num_acidentes

media_veiculos = soma_veiculos / cont
media_acidentes_2000 = soma_menor_2000 / cont_2000


print(f'\nMenor índice de acidentes:\n'
      f'A cidade {cod_menor_acidente} tem a menor taxa de acidentes totalizando {(menor_acidente/soma_acidentes)*100:.2f}%')
print(f'\nMaior índice de acidentes:\n'
      f'A cidade {cod_maior_acidente} tem a maior taxa de acidentes totalizando {(maior_acidente/soma_acidentes)*100:.2f}%')
print(f'\nA média de veículos das {cont} cidades juntas foi: {media_veiculos}')
print(f'\nA média de acidentes das cidades com menos de 2000 acidentes foi: {media_acidentes_2000:.2f}')






