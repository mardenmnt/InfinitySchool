"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudar_lado(self):
        troca = input(f'\nDeseja mudar o tamanho do lado atual? [s/n]\n').strip()[0].lower()

        if troca == "s":
            novo_lado = int(input("\n> Novo lado: "))
            self.lado = novo_lado
        else:
            print(f'\nOk o lado continua {self.lado}')

    def retornar_lado(self):
        print(f'\nO lado atual é {self.lado}')

    def calcular_area(self):
        pergunta = input(f'\nDeseja calcular a área? [s/n]\n').strip()[0].lower()

        if pergunta == "s":
            print(f'\nÁrea atual do quadrado: {self.lado * self.lado}') 
    

def main():

    quadrado = Quadrado(5)

    while True:
        quadrado.retornar_lado()
        quadrado.mudar_lado()
        quadrado.calcular_area()

        continuar = input('\nContinuar? [s/n]\n').strip()[0].lower()
        if continuar == "n":
            break

    quadrado.retornar_lado()

main()
