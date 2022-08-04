
-- count(*) conta todos os registros
-- count(nome_da_coluna) conta os registros mas ignora os nulos


SELECT * FROM ator;

SELECT * FROM ator ORDER BY primeiro_nome ASC;

SELECT * FROM ator ORDER BY primeiro_nome DESC;

SELECT primeiro_nome AS nome, ultimo_nome AS sobrenome FROM ator;

SELECT * FROM filme;

SELECT * FROM filme WHERE duracao_do_filme > 80;

SELECT * FROM filme WHERE classificacao = 'g';

SELECT * FROM filme WHERE preco_da_locacao < 2;

SELECT * FROM filme WHERE filme_id = 15;

SELECT * FROM filme WHERE preco_da_locacao < 2 AND classificacao = 'G';

SELECT COUNT(*) FROM filme WHERE preco_da_locacao < 2 AND classificacao = 'G';

SELECT * FROM filme WHERE duracao_do_filme > 120 OR preco_da_locacao > 1;

count

SELECT COUNT(*) FROM filme WHERE duracao_do_filme > 120 OR preco_da_locacao > 1;

SELECT COUNT(*) FROM filme;

SELECT COUNT(idioma_original_id) FROM filme;

SELECT COUNT(ator_id) FROM ator;
