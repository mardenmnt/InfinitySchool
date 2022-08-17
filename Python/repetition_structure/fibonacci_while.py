"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n-ésimo termo.
"""

termo_n = int(input("Informe o número de termos: "))

penultimo = 1
ultimo = 0
soma = 1
cont = 1
print("Fibonacci Series: ", end=" ")

if (termo_n == 1) or (termo_n == 2):
    print('1')
else:
    while cont <= termo_n:
        print(soma, end=" ")
        cont += 1
        penultimo = ultimo
        ultimo = soma
        soma = penultimo + ultimo
