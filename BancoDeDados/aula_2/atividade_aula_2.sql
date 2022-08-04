
-- FOREIGN KEY

CREATE TABLE Autores(
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
    autor VARCHAR(30)
);

CREATE TABLE Livros(
	id_livros INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR (50),
    fk_autor INT,
    FOREIGN KEY(fk_autor) REFERENCES Autores(id_autor)
);

ALTER TABLE Livros AUTO_INCREMENT = 50;

INSERT INTO autores(autor)
VALUES ('Paola Joséfina'), ('Reinaldo'), ('Felipe Agnaldo'), ('Antonia'), ('João');

INSERT INTO livros (titulo, fk_autor) VALUES ('Algoritmos', 5),
('BD', 1), ('Python', 3), ('C#', NULL), ('Java', 2);



-- JOINS


-- INNER JOIN (INTERSECÇÂO)
SELECT titulo, autor FROM livros INNER JOIN autores ON livros.fk_autor = autores.id_autor;


-- LEFT JOIN (TODOS autores independente se tem livro ou não)
SELECT titulo, autor FROM autores LEFT JOIN livros ON livros.fk_autor = autores.id_autor;


-- RIGHTJOIN (TODOS livros independente se tem autor cadastrado)
SELECT titulo, autor FROM autores RIGHT JOIN livros ON livros.fk_autor = autores.id_autor;

-- FULL JOIN não existe no MYSQL por isso usa-se RIGHT JOIN   UNION   LEFT JOIN
SELECT titulo, autor FROM autores RIGHT JOIN livros ON livros.fk_autor = autores.id_autor

UNION

SELECT titulo, autor FROM autores LEFT JOIN livros ON livros.fk_autor = autores.id_autor;
