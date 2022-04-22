"""
Crie um programa que leia 3 notas, calcule a média e informe se o aluno foi ou não aprovado:

Se média maior que 8 — aprovado com louvor
Se média maior que 6 e menor ou igual a 8 — aprovado
Se média maior que 4 e menor ou igual a 6 — recuperação
Se média abaixo de 4 — reprovado
"""
nota1 = float(input('informe a 1 nota: '))
nota2 = float(input('informe a 2 nota: '))
nota3 = float(input('informe a 3 nota: '))

# calculo da média
media = (nota1 + nota2 + nota3) / 3

# comparação da média com os parâmetros requisitados
if media > 8:
    print('Aprovado com louvor')
elif 6 < media <= 8:
    print('Aprovado')
elif 4 < media <= 6:
    print('Recuperação')
else:
    print('Reprovado')