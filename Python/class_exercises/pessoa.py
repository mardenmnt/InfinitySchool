"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        envelhece = input('Deseja envelhecer? [s/n]\n').strip()[0].lower()
        if envelhece == 's':
            anos = int(input('Quantos anos deseja envelhecer? '))
            self.idade += anos
            if self.idade < 21:
                self.altura += 0.5

    def engordar(self):
        engorda = input('Deseja engordar? [s/n]\n').strip()[0].lower()
        if engorda == 's':
            kg_ganhos = float(input('Quantos kg deseja ganhar? '))
            self.peso += kg_ganhos

    def emagrecer(self):
        engorda = input('Deseja emagrecer? [s/n]\n').strip()[0].lower()
        if engorda == 's':
            kg_perdidos = float(input('Quantos kg deseja perder? '))
            self.peso -= kg_perdidos

    def crescer(self):
        aumentar = input('Deseja crescer? [s/n]\n').strip()[0].lower()
        if aumentar == 's':
            cm = float(input('Quantos cm deseja crescer? '))
            self.altura += cm

    def pessoa_info(self):
        print(f'\nNome: {self.nome}\n'
      f'Idade: {self.idade}\n'
      f'Peso: {self.peso} Kg\n'
      f'Altura: {self.altura} cm\n')
       
if __name__ == '__main__':

    def main():

        nome = input(f'Nome: ')
        idade = int(input(f'Idade: '))
        peso = float(input(f'Peso: '))
        altura = int(input(f'Altura: '))

        pessoa = Pessoa(nome, idade, peso, altura)

        while True:
            pessoa.envelhecer()
            pessoa.engordar()
            pessoa.emagrecer()
            pessoa.crescer()

            continuar = input('\nContinuar? [s/n]\n').strip()[0].lower()
            if continuar == "n":
                break

        pessoa.pessoa_info()

    main()
