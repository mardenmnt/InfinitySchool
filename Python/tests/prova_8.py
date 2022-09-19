"""
Crie uma classe para armazenar as informações de um computador.
O computador deve ter os seguintes atributos:

-Modelo
-Fabricante
-Processador
-Memória RAM
-Tamanho do HD
-Espaço ocupado do HD
-Está ligado?

Sua classe também deve ter os seguintes métodos:

-liga() -> altera o status de "Está ligado" para True
-desliga() -> altera o status de "Está ligado" para False
-limparHD() -> recebe por parâmetro o tamanho do espaço que deseja liberar do HD
-ocuparHD() -> recebe por parâmetro o tamanho do espaço que deseja ocupar do HD

Lembre-se de manter as boas práticas na hora de criar os atributos, e certifique-se de que o
valor passado nos métodos "limparHD" e "ocuparHD" sejam válidos!
"""

# funcionamento

class Computador:
    def __init__(self, modelo, fabricante, processador, memoria, tam_hd, hd_ocupado = 0, ligado = False):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.memoria = memoria
        self.tam_hd = tam_hd
        self.hd_ocupado = hd_ocupado
        self.ligado = ligado

    def liga(self):
        if self.ligado == 's':
            print('\nComputador já está ligado!')
        elif self.ligado == 'n':
            self.ligado = 's'
            print('\nIniciando computador...')

    def desliga(self):
        if self.ligado == 'n':
            print('\nComputador já está desligado!')
        elif self.ligado == 's':
            self.ligado = 'n'
            print('\nDesligando computador...')

    def limpar_hd(self, tamanho):
        if self.ligado == 'n':
            print('Primeiro ligue o computador para gravar informações!')
        else:
            if tamanho > self.hd_ocupado:
                print(f'\nForam liberados {self.hd_ocupado}Gb, espaço do HD totalmente liberado')
            else:
                self.hd_ocupado -= tamanho
                print(f'\nForam liberados {tamanho}Gb, tamanho ocupado no Hd: {self.hd_ocupado}Gb')

    def ocupar_hd(self, tamanho):
        if self.ligado == 'n':
            print('Primeiro ligue o computador para gravar informações!')
        else:
            if tamanho > (self.tam_hd - self.hd_ocupado):
                print(f'\nSeu HD esta lotado! Libere espaço para gravar mais informações..')
            else:
                self.hd_ocupado += tamanho
                print(f'\nInformação armazenada com sucesso!')

# execução

if __name__ == '__main__':

    while True:
        print('\nInforme abaixo informações sobre seu computador:')
        modelo = input('Modelo: ')
        fabricante = input('Fabricante: ')
        processador = input('Processador: ')
        memoria = float(input('Total de Memória RAM: '))
        tam_hd = float(input('Tamanho total do HD: '))
        hd_ocupado = float(input('Total ocupado no HD: '))
        ligado = input('O computador esta ligado? sim/não\n').lower().strip()[0]

        if memoria <= 0 or tam_hd <= 0:
            print('Valores inválidos para QTD de memória ou HD, tente novamente')
            continue

        if hd_ocupado > tam_hd:
            print('O espaço ocupado maior que tamanho total do HD. Tente novamente')
            continue
        else:
            break

    computador = Computador(modelo, fabricante, processador, memoria, tam_hd, hd_ocupado, ligado)

    while True:
        print('\nEscolha uma das seguintes ações:\n'
              '[1] Ligar Computador\n'
              '[2] Desligar computador\n'
              '[3] Limpar HD\n'
              '[4] Ocupar HD\n'
              '[5] Sair')
        menu = input()

        if menu == '1':
            computador.liga()
        elif menu == '2':
            computador.desliga()
        elif menu == '3':
            excluir = float(input('Informe quantos Gb/Mb deseja excluir do HD: '))
            computador.limpar_hd(excluir)
        elif menu == '4':
            gravar = float(input('Informe quantos Gb/Mb deseja gravar no HD: '))
            computador.ocupar_hd(gravar)
        elif menu == '5':
            print('Encerrando sistema...')
            break
        else:
            print('Opção inválida! Tente novamente')
            continue
