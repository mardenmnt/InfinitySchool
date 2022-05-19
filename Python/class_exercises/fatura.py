"""
Crie uma classe chamada Invoice que possa ser utilizado por uma loja de suprimentos
de informática para representar uma fatura de um item vendido na loja. Uma fatura deve incluir as seguintes
informações como atributos:

• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.

Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade não for positiva, ela deve
ser configurada como 0. Se o preço por item não for positivo ele deve ser configurado como 0.0. Forneça
um método set e um método get para cada variável de instância. Além disso, forneça um método chamado
getInvoiceAmount que calcula o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e
depois retorna o valor como um double. Escreva um aplicativo de teste que demonstra as capacidades da
classe Invoice
"""


class Fatura:
    def __init__(self, num_item, descricao, qtd_item, valor):
        self.num_item = num_item
        self.descricao = descricao
        self.qtd_item = qtd_item
        self.valor = valor

        if qtd_item < 0:
            self.qtd_item = 0
        if valor < 0:
            self.valor = 0.0

    @property
    def numero_item(self):
        return self.num_item

    @numero_item.setter
    def numero_item(self, novo_numero):
        self.num_item = novo_numero

    @property
    def descricao_item(self):
        return self.descricao

    @descricao_item.setter
    def descricao_item(self, nova_descricao):
        self.descricao = nova_descricao

    @property
    def quantidade_item(self):
        return self.qtd_item

    @quantidade_item.setter
    def quantidade_item(self, nova_qtd):
        self.qtd_item = nova_qtd

    @property
    def valor_item(self):
        return self.valor

    @valor_item.setter
    def valor_item(self, novo_valor):
        self.valor = novo_valor

    def total_fatura(self):
        return float(self.qtd_item * self.valor)


fatura = Fatura(123, 'teste teste', 2, 20)

print(f'\nNúmero do item: {fatura.numero_item}')
print(f'Descrição do item: {fatura.descricao_item}')
print(f'QTD do item: {fatura.quantidade_item}')
print(f'Valor do item: {fatura.valor_item}')

print(f'Total: {fatura.total_fatura():.2f}')
