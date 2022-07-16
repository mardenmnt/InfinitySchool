
-- Criar uma tabela clientes. Esses clientes devem ser gerenciados pelos campos de CPF, Nome, Data de Nascimento, Endereço, CEP, Bairro, Cidade e UF
CREATE DATABASE exercicios;

USE exercicios;

CREATE TABLE clientes(
	cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(30),
    nascimento DATE,
    endereco VARCHAR(30),
    cep INT(8),
    bairro VARCHAR(20),
    cidade VARCHAR(20),
    uf VARCHAR(2)
);

-- Após criar a tabela acima especificada adicionar um campo para armazenar a data da última compra
ALTER TABLE clientes ADD ultima_compra DATE AFTER uf;

-- Inserir na tabela Clientes três clientes
INSERT INTO clientes (cpf, nome, nascimento, endereco, cep, bairro, cidade, uf)
VALUES 
('04496332780', 'João da Silva', 25/11/1969, 'Rua Antônio Numes', 88045963, 'Palmeiras', 'Londrina', 'PR'),
('05485031490', 'Ana Regina Fagundes', 21/09/1986, 'Rua Palmeias Novas', 88078923, 'Leblon', 'Rio de Janeiro', 'RJ'),
('03350314905', 'Fernando Soares', 05/03/1990, 'Rua Palmeias Novas', 88048917, 'Copacabana', 'Rio de Janeiro', 'RJ');

-- Selecionar todos os clientes que residam na cidade do Rio de Janeiro
SELECT * FROM clientes WHERE cidade = 'Rio de Janeiro';

-- Deletar os clientes que residam na cidade de Londrina
-- OBS: necessitou colocar cpf, devido o 'safe update' que necessita de uma primary key na condição
DELETE FROM clientes WHERE cidade = 'Londrina' and cpf = '04496332780';
