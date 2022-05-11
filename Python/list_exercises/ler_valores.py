"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

numeros = []
cont = 0
cont2 = 0
cont3 = 0
soma = 0

while True:
    num = float(input(f'{cont+1}º número: '))

    if num == -1:
        break
    else:
        cont += 1
        numeros.append(num)

# Mostre a quantidade de valores que foram lidos
print(cont)

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro
for i in numeros:
    print(i, end=' ')
    print('\n')
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro
numeros.reverse()
for j in numeros:
    print(j)
print('\n')

# Calcule e mostre a soma dos valores
print(f'{sum(numeros)}\n')

# Calcule e mostre a média dos valores
for k in numeros:
    soma += k
    media = soma/len(numeros)
print(f'{media}\n')

# Calcule e mostre a quantidade de valores acima da média calculada
for l in numeros:
    if l > media:
        cont2 += 1
print(f'{cont2}\n')

# Calcule e mostre a quantidade de valores abaixo de sete
for m in numeros:
    if m < 7:
        cont3 += 1
print(f'{cont3}\n')

# Encerre o programa com uma mensagem
print('***** FIM *****')
