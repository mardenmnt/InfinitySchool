"""
sala A
filhotes + não fivfelv + castrados + f/m
filhotes + não fivfelv + não castrados + f

sala B
adultos + não fivfelv + castrados + f/m

sala C
filhotes/adultos + não fivfelv + não castrados + m

sala D
filhotes/adultos + fivfelv + m

Outro local
filhote/adulto + fivfelv + castradas/não + f
"""

while True:
    idade = int(input('\nQual a idade do animal? '))
    castrado = input('O animal é castrado? [S]im/[N]ão ').upper().strip()[0]
    sexo = input('Qual sexo do animal? [M]acho/[F]êmea ').upper().strip()[0]
    fiv_felv = input('O animal testou positivo para FivFelv? [S]im/[N]ão ').upper().strip()[0]

    if idade <= 2 and fiv_felv == 'N' and castrado == 'N' and sexo == 'F':
        print('\nEncaminhe o animal para - Sala A')

    elif idade <= 2 and fiv_felv == 'N' and castrado == 'S' and (sexo == 'M' or sexo == 'F'):
        print('\nEncaminhe o animal para - Sala A')

    elif idade > 2 and fiv_felv == 'N' and castrado == 'S':
        print('\nEncaminhe o animal para - Sala B')

    elif fiv_felv == 'N' and castrado == 'N' and sexo == 'M':
        print('\nEncaminhe o animal para - Sala C')

    elif fiv_felv == 'S' and sexo == 'M':
        print('\nEncaminhe o animal para - Sala D')

    elif fiv_felv == 'S' and sexo == 'F':
        print('\nEsse animal deve ser encaminhado para outro gatil')

    pergunta = input('\nDeseja realizar nova consulta? [S]im/[N]ão ').upper().strip()[0]

    if pergunta == 'S':
        continue
    else:
        break
