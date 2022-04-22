"""
A cancela de um estabelecimento, neste momento de pandemia funciona dependendo da temperatura aferida e é
registrada pelo recepcionista do local. É preciso criar um algoritmo para liberar ou não cancela dependendo
da temperatura corporal. Com um medidor o recepcionista irá aferir e registrar no sistema e o algoritmo deverá
liberar caso a temperatura seja <= 37 e não liberar caso a temperatura seja maior que 37º.
A cancela só recebe True ou False (True para liberar e False para bloquear)
"""

temp = float(input('\nInforme a temperatura: ').replace(',', '.'))

# enviando informação para a cancela
if temp <= 37:
    cancela = True
else:
    cancela = False

# retornando o resultado obtido pela cancela
if cancela:  # if cancela == True -> if cancela  |  if cancela == False -> if not cancela
    print('Cancela liberada! Seja bem-vindo(a)')
else:
    print('Cancela bloqueada!\nSua temperatura está alta, procure um médico')
