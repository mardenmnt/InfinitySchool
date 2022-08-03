
CREATE TABLE aluno(
	nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(10),
    altura FLOAT(3,2),
    aprovado TINYINT(1)
);

INSERT INTO aluno (nome, email, telefone, altura, aprovado)
VALUES
('João das Neves', 'joão12345@gmail.com', '989456123', 2.00, 0),
('Maria das Flores', 'mariadasflores@gmail.com', '989456783', 1.60, 0),
('Cris Paiva', 'crispaiva@protonmail.com', '139456123', 1.70, 1),
('Dinho Arruda', 'dinhomail@gmail.com', '158964789', 1.80, 1),
('Mário Andrade', 'marioandrade@hotmail.com', '125654789', 1.72, 0),
('Herculano Júnior', 'herculano@gmail.com', '258964789', 1.75, 1),
('Anão do Dinho', 'anaofortal@gmail.com', '023456789', 1.20, 0);


-- SELECT


-- seleciona todos alunos com altura 1.8
SELECT * FROM aluno WHERE altura = 1.8;

-- seleciona todos alunos com altura diferente de 1.8
SELECT * FROM aluno WHERE NOT altura = 1.8;

-- seleciona todos alunos com altura 1.8
SELECT * FROM aluno WHERE altura != 1.8;

-- seleciona todos alunos com altura maior de 1.8
SELECT * FROM aluno WHERE altura > 1.8;

-- seleciona todos alunos com altura menor de 1.8
SELECT * FROM aluno WHERE altura < 1.8;

-- seleciona todos alunos com altura maior ou igual 1.8
SELECT * FROM aluno WHERE altura >= 1.8;

-- seleciona todos alunos com altura menor ou igual a 1.8
SELECT * FROM aluno WHERE altura <= 1.8;

-- seleciona todos alunos aprovados
SELECT * FROM aluno WHERE aprovado IS TRUE;

-- seleciona todos alunos reprovados
SELECT * FROM aluno WHERE aprovado IS FALSE;

-- seleciona todos alunos sem nome
SELECT * FROM aluno WHERE nome IS NULL;

-- seleciona todos alunos com nome
SELECT * FROM aluno WHERE nome IS NOT NULL;

-- seleciona todos alunos com altura entre 1.5 e 1.8
SELECT * FROM aluno WHERE altura BETWEEN 1.5 AND 1.8; 

-- seleciona todos alunos com altura fora do intervalo 1.5 e 1.8
SELECT * FROM aluno WHERE altura NOT BETWEEN 1.5 AND 1.8;

-- seleciona todos alunos com nome começando por Maria
SELECT * FROM aluno WHERE nome LIKE 'Maria%';

-- seleciona todos alunos com nome que não comece com Maria
SELECT * FROM aluno WHERE nome NOT LIKE 'Maria%';

-- seleciona todos alunos com uma das alturas
SELECT * FROM aluno WHERE altura IN (1.50, 1.60, 1.80, 1.70);

-- seleciona todos alunos com altura diferente das alturas
SELECT * FROM aluno WHERE altura NOT IN (1.50, 1.60, 1.80, 1.70);

-- seleciona todos alunos com altura menor que 1.8 e nome começando por Maria
SELECT * FROM aluno WHERE altura < 1.8 AND nome LIKE 'Maria%';

-- seleciona todos alunos com altura maior que 1.8 ou nome começando por Maria
SELECT * FROM aluno WHERE altura > 1.8 OR nome LIKE 'Maria%';

-- seleciona todos alunos com altura menor que 1.8 e nome não comece por Maria
SELECT * FROM aluno WHERE altura < 1.8 XOR nome LIKE 'Maria%';



-- ORDER BY

-- retorna todos alunos ordenados em ordem descrescente pela coluna aprovado
SELECT * FROM alunos ORDER BY aprovado DESC;

-- retorna todos em que aprovado = 1 ordenados pelo email, altura descercente e nome
SELECT * FROM alunos WHERE aprovado = 1 ORDER BY email, altura DESC, nome;
