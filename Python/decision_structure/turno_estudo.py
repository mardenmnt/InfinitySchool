"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print('\nDigite uma das opções abaixo:')
print('\n[M] - Matutino\n[V] - Vespertino\n[N] - Noturno')

turno = input('Qual turno você estuda? ').upper().strip()[0]

if turno == 'M':
    print('\nBom dia!')
elif turno == 'V':
    print('\nBoa tarde!')
elif turno == 'N':
    print('\nBoa noite!')
else:
    print('\nOpção inválida!')
