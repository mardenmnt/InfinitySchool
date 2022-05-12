"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios
"""

class ContaCorrente:
    def __init__(self, conta, nome, saldo = 0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self):
        alterar = input('Deseja alterar o nome? [s/n]').strip()[0].lower()
        if alterar == 's':
            novo_nome = input('\nNome: ')
            self.nome = novo_nome
            print('\nNome alterado com sucesso!')
    
    def depositar(self):
        deposito = input('Deseja realizar um depósito? [s/n]').strip()[0].lower()
        if deposito == 's':
            valor = float(input('Informe valor do depósito: '))
            self.saldo += valor
            print('Depósito realizado com sucesso!')
    
    def sacar(self):
        saque = input('Deseja realizar um saque? [s/n]').strip()[0].lower()
        if saque == 's':
            valor = float(input('Informe valor do saque: '))
            self.saldo -= valor
            print('\nSaque realizado com sucesso!')

if __name__ == '__main__':

    def main():

        nome = input('Nome: ')
        conta = input('Conta: ')
        saldo = float(input('Saldo: '))

        conta = ContaCorrente(nome, conta, saldo)

        while True:

            print('\n[1] Alterar nome\n[2] Depósito\n[3] Saque\n')
            operacao = input('Qual operação deseja realizar? ')

            if operacao == '1':
                conta.alterar_nome()
            elif operacao == '2':
                conta.depositar()
            elif operacao == '3':
                conta.sacar()
            else:
                print('Opção inválida, tente novamente!')
                continue

            outra = input('\nDeseja realizar outra operação? ').strip()[0].lower()

            if outra == 's':
                continue
            else:
                print('\nO banco agradece sua preferência até a próxima!')
                break

    main()
