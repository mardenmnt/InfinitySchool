"""
Mostre a sequência do número (INTEIRO) digitado pelo usuário até 100
"""



while True:
    num = int(input('Informe um numero até 100: '))
    if (num < 0) or (num > 100):
        print('Número inválido')
        continue
    else:
        while num <= 100:
            print(num)
            num += 1
    break
