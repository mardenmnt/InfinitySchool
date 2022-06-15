-- criando database mercado
CREATE DATABASE mercado;

USE mercado;

-- criando tabela produtos
CREATE TABLE produtos(
	cod_produto INT PRIMARY KEY,
    nome VARCHAR(30),
    categoria VARCHAR(20),
    preco FLOAT(8, 2)
);

-- criando database mercado
CREATE DATABASE clientes;

USE clientes;

-- criando tabela clientes
CREATE TABLE clientes(
	cod_cliente INT PRIMARY KEY,
    nome VARCHAR(25),
    endereço VARCHAR(30)
);

USE mercado;

-- inserindo produtos na tabela produtos
INSERT INTO produtos(cod_produto, nome, categoria, preco) VALUES(1, 'Mouse', 'Informática', 350);
INSERT INTO produtos(cod_produto, nome, categoria, preco) VALUES(2, 'Monitor', 'Informática', 1500);
INSERT INTO produtos(cod_produto, nome, categoria, preco) VALUES(3, 'Cadeira', 'Informática', 2500);
INSERT INTO produtos(cod_produto, nome, categoria, preco) VALUES(4, 'Casa', 'Imóvel', 500000);
INSERT INTO produtos(cod_produto, nome, categoria, preco) VALUES(5, 'Camisa', 'Vestuário', 50);
INSERT INTO produtos(cod_produto, nome, categoria, preco) VALUES(6, 'Mouse Gamer', 'Perifericos', 299.99);

-- UPDATE necessita de um parametro primary key no WHERE, caso contrário gera erro
-- gera erro
UPDATE produtos SET preco = 199.99 WHERE nome = 'Mouse Gamer';

-- para desativar usa-se -> SET SQL_SAFE_UPDATES = 0;
-- não é indicado o uso, por motivos de segurança

-- não gera erro
UPDATE produtos SET preco = 199.99 WHERE cod_produto = 6;

-- DELETE necessita de um parametro primary key no WHERE, caso contrário gera erro
-- gera erro
DELETE FROM produtos WHERE nome = 'mouse';

-- para desativar usa-se -> SET SQL_SAFE_UPDATES = 0;
-- não é indicado o uso, por motivos de segurança

-- não gera erro
DELETE FROM produtos WHERE cod_produto = 2;

DELETE FROM produtos WHERE cod_produto = 6;

-- exibindo dados com preco menor que 100
SELECT nome, categoria, preco FROM produtos WHERE preco < 100;

-- exibindo dados com codigo 1
SELECT nome, categoria, preco FROM produtos WHERE cod_produto = 1;

-- exibindo dados com nome 'mouse'
SELECT nome, categoria, preco FROM produtos WHERE nome = 'mouse';

-- exibindo dados com nome iniciado com letra 'm'
SELECT nome, categoria, preco FROM produtos WHERE nome LIKE 'm%';

-- exibindo dados com nome terminado com letra 'a'
SELECT nome, categoria, preco FROM produtos WHERE nome LIKE '%a';
