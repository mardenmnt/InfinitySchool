"""
Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
Escreva um pequeno programa que teste sua classe
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def devolve_nome(self):
        return self.nome

    @property
    def devolve_salario(self):
        return self.salario


funcionario = Funcionario('Ana', 1500)

print(f'\nNome: {funcionario.devolve_nome}')
print(f'Salário: {funcionario.devolve_salario}')


print('-='*20)

"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que
aumente o salário do funcionário em uma certa porcentagem.

Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
"""


class Funcionario2:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def devolve_nome(self):
        return self.nome

    @property
    def devolve_salario(self):
        return self.salario

    def aumentar_salario(self, aumento):
        self.salario += self.salario * (aumento / 100)


funcionario = Funcionario2('Ana', 1500)

print(f'Nome: {funcionario.devolve_nome}')
print(f'Salário: {funcionario.devolve_salario:.2f}')

funcionario.aumentar_salario(10)

print(f'\nNome: {funcionario.devolve_nome}')
print(f'Salário: {funcionario.devolve_salario:.2f}')
