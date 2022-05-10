"""
Crie um programa que leia altura, peso, calcule o IMC e informe o estado em que a pessoa se encontra:
Se IMC < 18.5 — subnutrido
Se IMC entre 18.5 e 24.9 — normal
Se IMC entre 25 e 29.9 — sobrepeso
Se IMC entre 30 e 34.9 — obesidade nivel 1
Se IMC entre 35 e 39.9 — obesidade nivel 2
Se IMC maior ou igual a 40 — obesidade nivel 3
"""

print('\nCalcule seu IMC')
peso = float(input('Informe seu peso: ').replace(',', '.'))
altura = float(input('Informe sua altura: ').replace(',', '.'))

# calculo do IMC
imc = peso / (altura ** 2)

# definindo o tipo de IMC
if imc < 18.5:
    print('\nSeu IMC é:', imc, 'procure um médico você está subnutrido')
elif 18.5 <= imc < 24.9:
    print('\nSeu IMC é:', imc, 'e está normal')
elif 25 <= imc < 29.9:
    print('\nSeu IMC é:', imc, 'e está com sobrepeso')
elif 30 <= imc < 34.9:
    print('\nSeu IMC é:', imc, 'cuidado você está com obesidade grau I')
elif 35 <= imc < 39.9:
    print('\nSeu IMC é:', imc, 'cuidado você está com obesidade grau II')
elif imc >= 40:
    print('\nSeu IMC é:', imc, 'procure um médico você está com obesidade grau III')
