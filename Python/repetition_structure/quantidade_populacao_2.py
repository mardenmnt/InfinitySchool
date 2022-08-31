"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

contador = 0

while True:
    populacao_a = int(input('Informe a quantidade de população do 1º país: '))
    taxa_a = float(input('Informe a taxa de crescimento do 1ºpaís: ').replace(',', '.'))
    populacao_b = int(input('Informe a quantidade de população do 2º país: '))
    taxa_b = float(input('Informe a taxa de crescimento do 1ºpaís: ').replace(',', '.'))

    if populacao_a <= 0 and populacao_b <= 0 and taxa_a <= 0 and taxa_b <= 0:
        print('Quantidade de população e/ou taxa inválido(s)\n'
              'Por favor, informe um número maior que zero')
        continue
    while populacao_a <= populacao_b:
        populacao_a = populacao_a + (populacao_a * taxa_a)
        populacao_b = populacao_b + (populacao_b * taxa_b)
        contador += 1
        print(f"No ano {contador}:")
        print(f"A população de A será: {populacao_a}.")
        print(f"A população de B será: {populacao_b}.")
    break

print(f"\nDepois de {contador} anos, a população de A passará a populaçao de B.")
