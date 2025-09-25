DROP TABLE IF EXISTS candidatos;
CREATE TABLE candidatos (
    id_candidato INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    salario_mensal DECIMAL(10, 2),
    idade INTEGER,
    departamento VARCHAR(50),
    salario_anual DECIMAL(10, 2)
);
