"""
Crie programa que receba quantidade de eleitores de um município,
a quantidade de votos em branco, nulos e válidos. Por fim exiba o percentual
dos votos em relação à quantidade de votos em branco, válidos e nulos
"""

eleitores = int(input('Informe a quantidade de eleitores no seu município: '))
brancos = int(input('Informe a quantidade de votos brancos: '))
nulos = int(input('Informe a quantidade de votos nulos: '))
validos = int(input('Informe a quantidade de votos válidos: '))

print('\nO percentual dos votos em relação a quantidade de eleitores:')
print('Votos válidos:', round((validos/eleitores) * 100, 3), '%')
print('Votos em branco:', round((brancos/eleitores) * 100, 3), '%')
print('Votos nulos:', round((nulos/eleitores) * 100, 3), '%')
print('* A margem de erro é de dois pontos percentuais para mais ou para menos *')
