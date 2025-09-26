# Importando as bibliotecas necessárias
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# --- FASE DE EXTRAÇÃO E TRANSFORMAÇÃO ---

dados_brutos = {
    'id_candidato': [1, 2, 3, 4, 5, 6],
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'ELIANA', 'Fernando'],
    'data_nascimento': ['1992-03-15', '1988-08-20', '1995-01-30', '1992-07-11', '1990-12-25', '1985-05-01'],
    'salario_mensal': [5000, 6500, None, 7200, 6800, 9500],
    'departamento': ['tecnologia', 'marketing', 'Tecnologia', 'Vendas', 'vendas', 'marketing']
}

df = pd.DataFrame(dados_brutos)

# Limpeza e Transformação
mediana_salario = df['salario_mensal'].median()
df['salario_mensal'] = df['salario_mensal'].fillna(mediana_salario)
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'])
ano_atual = datetime.now().year
df['idade'] = ano_atual - df['data_nascimento'].dt.year
df['nome'] = df['nome'].str.title()
df['departamento'] = df['departamento'].str.upper()
df['salario_anual'] = df['salario_mensal'] * 12

# --- FASE DE CARGA (LOAD) ---

# ⚠️ Lembre-se de usar sua senha real do Postgres aqui
connection_string = 'postgresql://postgres:Jasopa20@localhost:5432/postgres'
engine = create_engine(connection_string)

# Usaremos 'replace' aqui para que a cada execução a tabela seja substituída.
# Em um pipeline real, 'append' seria mais comum para novos dados.
df.to_sql(
    'candidatos',
    engine,
    if_exists='replace', # Isso vai apagar a tabela e inserir os novos dados
    index=False
)

# Mensagem de sucesso que será capturada no log
print(f"Pipeline ETL executado com sucesso em: {datetime.now()}")
