-- retorna contagem de todos aprovados e reprovados separados por grupo

CREATE TABLE alunos(
	nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(10),
    altura FLOAT(3,2),
    sexo VARCHAR(1),
    aprovado TINYINT(1)
);

INSERT INTO alunos (nome, email, telefone, altura, aprovado)
VALUES
('João das Neves', 'joão12345@gmail.com', '989456123', 2.00, 'M', 0),
('Maria das Flores', 'mariadasflores@gmail.com', '989456783', 'F', 1.60, 0),
('Cris Paiva', 'crispaiva@protonmail.com', '139456123', 1.70, 'F', 1),
('Dinho Arruda', 'dinhomail@gmail.com', '158964789', 1.80, 'M', 1),
('Mário Andrade', 'marioandrade@hotmail.com', '125654789', 1.72, 'M', 0),
('Herculano Júnior', 'herculano@gmail.com', '258964789', 1.75, 'M', 1),
('Anão do Dinho', 'anaofortal@gmail.com', '023456789', 1.20, 'M', 0);


-- retorna contagem de todos aprovados e reprovados separados por grupo
SELECT aprovado, COUNT(*) FROM alunos GROUP BY aprovado;

-- retorna contagem de sexo e aprovados ordenados por sexo e aprovado
SELECT sexo, aprovado, COUNT(*) FROM alunos GROUP BY sexo, aprovado;

-- retorna contagem de reprovados com nome começando com M e não terminando com A agrupados por aprovado
SELECT COUNT(*) AS total_aprovados FROM alunos WHERE aprovado = 0 AND nome LIKE 'M%' XOR '%A' GROUP BY aprovado;

-- retorna valores únicos de uma coluna, desprezando valores duplicados
SELECT DISTINCT sexo FROM alunos;

-- limita a quantidade de exibição da pesquisa
SELECT * FROM alunos LIMIT 5;

-- descarta os 5 primeiros registros e o resultado conterá no máximo 2 registros
SELECT * FROM alunos LIMIT 5, 2;
