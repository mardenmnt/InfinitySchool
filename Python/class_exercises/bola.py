"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__(self, cor, circunf, material):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input(f'Deseja mudar a cor atual {self.cor}? [s/n]')

        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.cor = nova_cor
        else:
            print(f'Ok a cor continua {self.cor}')

    def mostraCor(self):
        print(f'\nA cor atual é {self.cor}')


def main():
    bola = Bola("azul", 5, "metal")

    while True:
        bola.mostraCor()
        bola.trocaCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola.mostraCor()


main()
