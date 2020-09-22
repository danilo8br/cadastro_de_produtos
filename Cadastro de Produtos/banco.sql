# TABELA CATEGORIA
CREATE TABLE categoria (
	id_categoria INT NOT NULL AUTO_INCREMENT,
    tipo_categoria VARCHAR(20),
    CONSTRAINT PK_categoria PRIMARY KEY (id_categoria)
);

# TABELA PRODUTOS
CREATE TABLE produtos (
	id INT NOT NULL AUTO_INCREMENT,
    codigo VARCHAR(50),
    preco DECIMAL(8,2),
    descricao VARCHAR(50),
	id_categoria INT,
    CONSTRAINT PK_produtos PRIMARY KEY (id),
    CONSTRAINT PK_produtos_categoria FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
);
    
# SELECIONANDO AS TABELAS    
SELECT id, codigo, preco, descricao, tipo_categoria 
FROM produtos 
INNER JOIN categoria ON produtos.id = categoria.id_categoria;

# INSERINDO OS PRODUTOS
SELECT id, codigo, preco, descricao, tipo_categoria 
FROM produtos 
INNER JOIN categoria ON produtos.id = categoria.id_categoria;

# ALTERANDO OS PRODUTOS
UPDATE produtos SET descricao = 'PS5', preco = 1500.00 WHERE codigo = 1;

# EXCLUINDO OS PRODUTOS
DELETE FROM produtos WHERE codigo = 1;

# USANDO O BANCO
USE lojinha;

