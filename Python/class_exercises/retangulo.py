"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local
"""

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self):
        mudar = input('\nDeseja mudar algum dos lados? [s/n]\n')

        if mudar == 's':
            self.base = float(input('\n> Base: '))
            self.altura = float(input('> Altura: '))
        else:
            print('Ok, os tamanhos permanecem os mesmos')
    
    def retornar_valor(self):
        print(f'\nBase: {self.base}\n'
              f'Altura: {self.altura}')
    
    def calcular_area(self):
        pergunta = input('Deseja calcular a área? [s/n]\n').strip()[0].lower()

        if pergunta == 's':
            area = self.base * self.altura
            print(f'\nA área vale {area}')
        
    def calcular_perimetro(self):
        pergunta2 = input('Deseja calcular o perímetro? [s/n]\n').strip()[0].lower()

        if pergunta2 == 's':
            perimetro = (self.base * 2) + (self.altura * 2)
            print(f'\nO perímetro vale {perimetro}')

def main():
    retangulo = Retangulo(5, 5)

    while True:
        retangulo.retornar_valor()
        retangulo.mudar_lados()
        retangulo.calcular_area()
        retangulo.calcular_perimetro()

        continua = input('Deseja continuar? [s/n]\n').strip()[0].lower()

        if continua == 'n':
            break

    retangulo.retornar_valor()

main()
