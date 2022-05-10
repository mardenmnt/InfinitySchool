"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante"""

letra = input('\nInforme uma letra: ')

vogais = ['a', 'e', 'i', 'o', 'u']

# criando uma lista de números
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

if letra in vogais:
    print('Essa letra é uma vogal')
# tratando possível erro ao usuário digitar número
elif letra in num:
    print('Você digitou um número e não uma letra')
else:
    print('Essa letra é uma consoante')
