"""
Faça um algoritmo que calcule a quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores davelocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
"""

import math

# entradas
tempo = float(input('Informe o tempo da viagem: '))
velocidade = float(input('Agora informe a velocidade média: '))

# cálculos
distancia = tempo * velocidade
litros_usados = distancia / 12

# math.modf quebra o float em inteiro e fração
frac, inteiro = math.modf(tempo)  # frac pega a parte inteira
print(frac)  # inteiro pega parte inteira
print(inteiro)

#saídas
print(f'\nO veículo percorreu a distância de {round(distancia, 2)}km')
print(f'Velocidade média {velocidade}km/h')
print(f'Foram utilizados {round(litros_usados, 2)} L de combustível')
print(f'Tempo da viagem foi de aproximadamente {int(inteiro)} horas e {round(frac * 100)} minutos')
