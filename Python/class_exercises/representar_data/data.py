"""
Crie uma classe para representar datas.
1. Represente uma data usando três atributos: o dia, o mês, e o ano.
2. Sua classe deve ter um construtor que inicializa os três atributos e verifica a validade dos valores
fornecidos.
3. Forneça um construtor sem parâmetros que inicializa a data com a data atual fornecida pelo sistema
operacional.
4. Forneça um método set um get para cada atributo.
5. Forneça o método toString para retornar uma representação da data como string. Considere que a
data deve ser formatada mostrando o dia, o mês e o ano separados por barra (/).
6. Forneça uma operação para avançar uma data para o dia seguinte.
7. Escreva um aplicativo de teste que demonstra as capacidades da classe.
Garanta que uma instância desta classe sempre esteja em um estado consistente
"""


class Data:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def to_string(self):
        print(f'Data atual: {self.__dia}/{self.__mes}/{self.__ano}')

    def avancar_dia(self, dia, mes, ano):
        if dia >= 31 and mes in [1, 3, 5, 7, 8, 10]:
            self.__dia, self.__mes = 1, self.__mes + 1

        elif dia >= 31 and mes == 12:
            self.__dia, self.__mes, self.__ano = 1, 1, self.__ano + 1

        elif dia >= 30 and mes in [2, 4, 6, 9, 11]:
            self.__dia, self.__mes = 1, self.__mes + 1
        else:
            self.__dia += 1

    def mudar_data(self):
        while True:
            self.__dia = int(input('Dia: ').strip())
            if self.__dia <= 0 or self.__dia > 31:
                print('Dia inválido! Tente novamente')
                continue
            self.__mes = int(input('Mês: ').strip())
            if self.__mes <= 0 or self.__mes > 12:
                print('Mês inválido! Tente novamente')
                continue
            self.__ano = int(input('Ano: ').strip())
            if self.__ano <= 0:
                print('Ano inválido! Tente novamente')
                continue
            print('Data modificada com sucesso!\n')
            break
