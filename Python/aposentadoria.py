"""
Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não.
Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
1) Ter no mínimo 65 anos de idade.
2) Ter trabalhado no mínimo 30 anos.
3) Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código),
o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho do
empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'
"""

codigo = input('\nInforme o número do empregado: ')
nascimento = int(input('Informe o ano de nascimento: '))
ingresso = int(input('Informe o ano de ingresso na empresa: '))

ano_atual = 2022
idade = ano_atual - nascimento
tempo_trabalho = ano_atual - ingresso

if idade >= 65 or tempo_trabalho >= 30 or (idade >= 60 and tempo_trabalho >= 25):
    print(f'Você tem {idade} anos e {tempo_trabalho} anos de trabalho')
    requisita = input('Deseja requerer aposentadoria ? Digite [S] ou [N]: ').upper()
    if requisita == 'S':
        print('\nSua aposentadoria foi requisitada com êxito!')
    elif requisita == 'N':
        print('\nOperação finalizada')
    else:
        print('\nOpção inválida')
else:
    print('\nVocê ainda não possui os requisitos mínimos para aposentadoria')
    print('''\nRequisitos mínimos para requisitar aposentadoria:
1) Ter no mínimo 65 anos de idade.
2) Ter trabalhado no mínimo 30 anos.
3) Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.''')



