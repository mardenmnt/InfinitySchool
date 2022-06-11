"""
Crie um algoritmo que recebe como entrada o dia e o mês de nascimento e retorna o signo, seguindo as faixas de valores informados:
- Áries: de 21 março a 20 abril;
- Touro: de 21 abril a 20 maio;
- Gêmeos: de 21 maio a 20 junho;
- Câncer: de 21 junho a 22 julho;
- Leão: de 23 julho a 22 agosto;
- Virgem: de 23 agosto a 22 setembro;
- Libra: de 23 setembro a 22 outubro;
- Escorpião: de 23 outubro a 21 novembro;
- Sagitário: de 22 novembro a 21 dezembro;
- Capricórnio: de 22 dezembro a 20 janeiro;
- Aquário: de 21 janeiro a 18 fevereiro;
- Peixes: de 19 fevereiro a 20 março.
"""


# entradas
dia = int(input('\nInforme o dia que você nasceu: '))
mes = int(input('Agora informe o mês que você nasceu: '))

# tratando erro data inválida
while (dia <= 0 or dia > 31) or (mes <= 0 or mes > 12) or (dia > 28 and mes == 2):
    print('Dia ou mês incorretos, por favor confira as informações')
    dia = int(input('\nInsira o dia que você nasceu: '))
    mes = int(input('Insira o mês que você nasceu: '))

# condições dos signos
if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
    print(f'{dia}/{mes} - Signo de Áries')
elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
    print(f'{dia}/{mes} - Signo de Touro')
elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
    print(f'{dia}/{mes} - Signo de Gêmeos')
elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
    print(f'{dia}/{mes} - Signo de Câncer')
elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
    print(f'{dia}/{mes} - Signo de Leão')
elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
    print(f'{dia}/{mes} - Signo de Virgem')
elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
    print(f'{dia}/{mes} - Signo de Libra')
elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
    print(f'{dia}/{mes} - Signo de Escorpião')
elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
    print(f'{dia}/{mes} - Signo de Sargitário')
elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
    print(f'{dia}/{mes} - Signo de Capricórnio')
elif (dia >= 21 and mes == 1) or (dia <= 18 and mes == 2):
    print(f'{dia}/{mes} - Signo de Aquário')
elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
    print(f'{dia}/{mes} - Signo de Peixes')
