
"""
Refaça o programa utilizando as seguintes condições:

se a temperatura for menor que 20 -> muito frio
se a temperatura estiver entre 20 e 30 -> Normal
se estiver acima de 31 -> quente
acima de 38-> PEGANDO FOGO!
"""

temp_f = float(input('Informe uma temperatura em Fahrenheit: '))

temp_cel = 5 * ((temp_f - 32) / 9)

if temp_cel <= 20:
    print(f'{temp_cel:.2f}ºC - muito frio')
elif 20 < temp_cel <= 30:
    print(f'{temp_cel:.2f}ºC - normal')
elif 31 < temp_cel <= 38:
    print(f'{temp_cel:.2f}ºC - quente')
else:
    print(f'{temp_cel:.2f}ºC - pegando fogo')
