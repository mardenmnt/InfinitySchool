CREATE DATABASE livraria;

USE livraria;

CREATE TABLE editora(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);


CREATE TABLE livro(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    preco FLOAT(5, 2) NOT NULL
);

INSERT INTO editora(nome, email) VALUES ('Oreilly', 'oreilly@email.com');
INSERT INTO editora(nome, email) VALUES ('Wrox', 'wrox@email.com');
INSERT INTO editora(nome, email) VALUES ('Apress', 'apress@email.com');

INSERT INTO livro(titulo, preco) VALUES('Aprendendo Python', 89.90);
INSERT INTO livro(titulo, preco) VALUES('Introdução ao JSF 2', 122.90);
INSERT INTO livro(titulo, preco) VALUES('JSF 2 Avançado', 149.90);

SELECT * FROM livro;

UPDATE livro SET preco = 92 WHERE id = 1;

UPDATE editora SET nome = 'OReilly' WHERE id = 1;

DELETE FROM livro WHERE id = 2;
