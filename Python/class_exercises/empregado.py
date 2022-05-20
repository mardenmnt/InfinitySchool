""" A fim de representar empregados em uma firma, crie uma classe chamada Empregado que
inclui as três informações a seguir como atributos:

• um primeiro nome,
• um sobrenome, e
• um salário mensal.

Sua classe deve ter um construtor que inicializa os três atributos. Forneça um método set e get para cada
atributo. Se o salário mensal não for positivo, configure-o como 0.0. Escreva um aplicativo de teste que
demonstra as capacidades da classe. Crie duas instâncias da classe e exiba o salário anual de cada instância.
Então dê a cada empregado um aumento de 10% e exiba novamente o salário anual de cada empregado
"""


class Empregado:
    def __init__(self, primeiro, sobrenome, salario):
        self.__primeiro = primeiro
        self.__sobrenome = sobrenome
        self.__salario = salario

        if salario < 0:
            self.__salario = 0.0

    @property
    def primeiro_nome(self):
        return self.__primeiro

    @primeiro_nome.setter
    def primeiro_nome(self, novo_primeiro_nome):
        self.__primeiro = novo_primeiro_nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self.__sobrenome = novo_sobrenome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario

    def aumentar_salario(self, aumento):
        self.__salario += (self.salario * (aumento/100))


empregado1 = Empregado('Carlos', 'Antonio', -1)

empregado2 = Empregado('Carla', 'Dias', 1000)

print(f'\n{empregado1.primeiro_nome} {empregado1.sobrenome}\n'
      f'Salário Mensal: R$ {empregado1.salario:.2f}\n'
      f'Salário Anual: R$ {empregado1.salario * 12:.2f}\n')
print(f'{empregado2.primeiro_nome} {empregado2.sobrenome}\n'
      f'Salário Mensal: R$ {empregado2.salario:.2f}\n'
      f'Salário Anual: R$ {empregado2.salario * 12:.2f}')

print('-='*20)
empregado1.aumentar_salario(10)
empregado2.aumentar_salario(10)

print(f'{empregado1.primeiro_nome} {empregado1.sobrenome}\n'
      f'Salário Mensal: R$ {empregado1.salario:.2f}\n'
      f'Salário Anual: R$ {empregado1.salario*12:.2f}\n')
print(f'{empregado2.primeiro_nome} {empregado2.sobrenome}\n'
      f'Salário: R$ {empregado2.salario:.2f}\n'
      f'Salário Anual: R$ {empregado2.salario * 12:.2f}\n')
