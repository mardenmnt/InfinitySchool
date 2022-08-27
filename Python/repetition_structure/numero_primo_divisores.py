"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1

Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""

num = int(input('Informe um número inteiro: '))
# num é primo até que se prove o contrário
e_primo = True
# procure por um divisor de num entre 2 e num - 1
divisor = 2

while divisor < num and e_primo:        # equivalente a "div... and é_primo == True:"
    if num % divisor == 0:
        e_primo = False
    divisor += 1

if e_primo and num != 1:        # 1 não é primo
    print(f'{num}, é primo')
else:
    print(f'O número {num}, não é primo')
    print(f'Ele é divisível por:')
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=' ')
