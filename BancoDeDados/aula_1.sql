
-- "DROP" (Excluir database)
DROP DATABASE test;

-- "CREATE" (Criar database)
CREATE DATABASE escola;

-- "USE" (Utilizar database desejado)
USE escola;

-- Criar tabela:
-- nome da coluna,
-- tipo da coluna (INT, VARCHAR, FLOAT),
-- atributos (não obrigatório))

-- FLOAT recebe 2 parametros (qtd de digitos, qtd de casas decimais)
CREATE TABLE alunos(
	matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nota FLOAT(3, 1),
    curso VARCHAR(20)
);

CREATE TABLE professores(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    area VARCHAR(20),
    salario FLOAT(7, 2)
);


-- Alterar tabela(adicionar coluna, remover coluna, alterar coluna, renomear coluna)

-- adicionar coluna
ALTER TABLE alunos ADD COLUMN idade INT(2);

-- adicionar coluna
ALTER TABLE alunos ADD COLUMN teste INT(2);

-- excluir coluna
ALTER TABLE alunos DROP COLUMN teste;

-- alterar coluna
ALTER TABLE professores MODIFY COLUMN salario FLOAT(8,2);

-- alterar nome da coluna
ALTER TABLE professores CHANGE nome nome_professor VARCHAR(30);

-- alterar nome do database
RENAME TABLE professores TO professor;

-- excluir tabela
DROP TABLE professor;

-- CRUD (inserir dados, atualizar dados, excluir dados, buscar dados)

-- inserir valores
INSERT INTO alunos(matricula, nome, curso, nota)
VALUES(001, 'Marden', 'Python', 8.2);

INSERT INTO professor(id, nome_professor, area, salario)
VALUES(001, 'Bruno', 'Design', 4500),
(002, 'Grazy', 'Dev', 6600);

-- mostrar dados da tabela professor
SELECT * FROM professor;

-- mostrar dados da tabela alunos
SELECT * FROM alunos;
