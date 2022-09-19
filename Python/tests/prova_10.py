"""
Fazendo parte de um time de desenvolvedores, foi atribuído a você o desenvolvimento de um módulo de um sistema de empresas
que pagam tributos às prefeituras.

Cada empresa cadastrada com o nome, cnpj, média de funcionários, e média de lucro mensal.

As prefeituras devem ser cadastradas com cidade, prefeito(a) e valor total de impostos.

O(a) prefeito(a) deve ser cadastrado também com nome, cpf e formação.

A prefeitura pode ter várias empresas as quais coleta impostos.

Cada empresa deve fornecer 1.6% de seus lucros mensais para a prefeitura associada e
deve ser feito o cálculo a partir desta informação de todas as empresas de uma prefeitura,
quanto pagam mensalmente, pois este será o valor total de impostos
"""


class Empresa:
    def __init__(self, nome, cnpj, media_func, media_lucro_mensal):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__media_func = media_func
        self.__media_lucro_mensal = media_lucro_mensal

    @property
    def nome(self):
        return self.__nome

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def media_func(self):
        return self.__media_func

    @property
    def media_lucro_mensal(self):
        return self.__media_lucro_mensal

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj

    @media_func.setter
    def media_func(self, novo_media_func):
        self.__media_func = novo_media_func

    @media_lucro_mensal.setter
    def media_lucro_mensal(self, novo_media_lucro_mensal):
        self.__media_lucro_mensal = novo_media_lucro_mensal

    def imposto(self, total):
        self.__media_lucro_mensal = (1.6 / 100) * total
        return self.__media_lucro_mensal


class Prefeitura:
    def __init__(self, cidade, prefeito):
        self.__cidade = cidade
        self.__prefeito = prefeito
        self.__valor_total_imposto = empresa.imposto(sum(impostos))

    @property
    def cidade(self):
        return self.__cidade

    @property
    def prefeito(self):
        return self.__prefeito

    @prefeito.setter
    def prefeito(self, novo_prefeito):
        self.__prefeito = novo_prefeito

    def imposto_arrecadar(self):
        return self.__valor_total_imposto



class Prefeito:
    def __init__(self, nome, cpf, formacao):
        self.__nome = nome
        self.__cpf = cpf
        self.__formacao = formacao

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def formacao(self):
        return self.__formacao

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @formacao.setter
    def formacao(self, nova_formacao):
        self.__formacao = nova_formacao


if __name__ == '__main__':

    impostos = []

    while True:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('*       CADASTRO DE EMPRESA            *')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        nome = input('Nome da empresa: ')
        cnpj = int(input('CNPJ: '))
        media_func = int(input('Média de funcionários: '))
        media_lucro_mensal = float(input('Média lucro mensal: '))

        empresa = Empresa(nome, cnpj, media_func, media_lucro_mensal)
        impostos.append(empresa.media_lucro_mensal)

        continuar = input('Deseja cadastrar outra empresa? s/n\n').lower().strip()[0]

        if continuar == 's':
            continue
        else:
            break

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('*       PREFEITURA RESPONSÁVEL         *')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    cidade = input('Informa a cidade onde essa(s) empresas estão alocadas: ')
    prefeito = input('Informe o nome do prefeito responsável: ')

    prefeitura = Prefeitura(cidade, prefeito)

    print(f'\nO total de impostos a arrecadar na prefeitura de {cidade} é de R${prefeitura.imposto_arrecadar():.2f}')
