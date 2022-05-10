"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""

down = float(input('Informe o tamanho do arquivo em MB: ').replace(',', '.'))
vel = float(input('Informe a velocidade da internet em Mbps: ').replace(',', '.'))

# Mbps (megabits por segundo) para MB/s (megabytes por segundo)
# você deve dividir o valor por oito e o contrário é multiplicar por oito

# conversão de MB/s para Mbps
down_mb = down * 8

# cálculo da velocidade
tempo_segundos = down_mb / vel

# conversão de segundos para minutos
tempo_minutos = tempo_segundos / 60

print(f'\nTempo aproximado para download: {tempo_minutos:.2f} minuto(s)')
