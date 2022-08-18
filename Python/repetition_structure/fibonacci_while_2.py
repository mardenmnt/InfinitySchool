"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500
"""
v1 = 0
v2 = 1
termos = int(input('Digite a quantidade de termos: '))
cont = 0

if termos <= 0:
    print('Quantidade de termos inválida!!')
elif termos == 1:
    print(v1)
else:
    while cont < termos:
        print(v1, end=' ')
        v3 = v1 + v2
        v1 = v2
        v2 = v3
        cont += 1
