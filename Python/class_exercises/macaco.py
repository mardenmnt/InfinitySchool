"""
Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        print('Comendo...')
        self.bucho.append(alimento)

    def ver_bucho(self):
        for i in self.bucho:
            print(i)

    def digerir(self):
        print('Digerindo...')
        self.ver_bucho()
        self.bucho = []


if __name__ == '__main__':
    def main():
        while True:
            nome = input('Informe o nome do macaco: ')

            macaco = Macaco(nome)

            while True:
                print('Escolha uma opção:\n'
                      '[1] Comer\n'
                      '[2] Ver bucho\n'
                      '[3] Digerir\n')
                opcao = input()

                if opcao == '1':
                    alimento = input('\nQual alimento deseja comer? ')
                    macaco.comer(alimento)
                elif opcao == '2':
                    macaco.ver_bucho()
                elif opcao == '3':
                    macaco.digerir()
                else:
                    print('\nOpção inválida!')

                continuar = input('\nDeseja continuar? [s/n]\n').lower().strip()[0]

                if continuar == 's':
                    continue
                else:
                    break

            troca = input('Deseja trocar de macaco? [s/n]\n').lower().strip()[0]
            if troca == 's':
                continue
            else:
                break
                
    main()
