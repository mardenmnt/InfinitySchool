
CREATE TABLE alunos(
	nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(10),
    altura FLOAT(3,2),
    aprovado TINYINT(1)
);

INSERT INTO alunos (nome, email, telefone, altura, aprovado)
VALUES
('João das Neves', 'joão12345@gmail.com', '989456123', 2.00, 0),
('Maria das Flores', 'mariadasflores@gmail.com', '989456783', 1.60, 0),
('Cris Paiva', 'crispaiva@protonmail.com', '139456123', 1.70, 1),
('Dinho Arruda', 'dinhomail@gmail.com', '158964789', 1.80, 1),
('Mário Andrade', 'marioandrade@hotmail.com', '125654789', 1.72, 0),
('Herculano Júnior', 'herculano@gmail.com', '258964789', 1.75, 1),
('Anão do Dinho', 'anaofortal@gmail.com', '023456789', 1.20, 0);


-- conta quantidade de alunos
SELECT COUNT(*) FROM alunos;

-- retorna a média das alturas
SELECT AVG(altura) FROM alunos;

-- retorna a soma das alturas
SELECT SUM(altura) FROM alunos;

-- retorna a maior altura
SELECT MAX(altura) FROM alunos;

-- retorna a menor altura
SELECT MIN(altura) FROM alunos;

-- retorna a variância das alturas
SELECT VARIANCE(altura) FROM alunos;

-- retorna a desvio padrão
SELECT STD(altura) FROM alunos;

-- retorna desvio padrão (esse comando é para compatibilidade com Oracle)
SELECT STDDEV(altura) FROM alunos;

-- calcula a média das alturas dos alunos reprovados
SELECT AVG(altura) FROM alunos WHERE aprovado = 0;

-- calcula a variância das alturas 
SELECT VARIANCE(altura) FROM alunos WHERE altura > 1.7;
