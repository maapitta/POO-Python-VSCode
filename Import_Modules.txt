# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

# Cria a tabela FILME no banco de dados
connection.execute('''CREATE TABLE IF NOT EXISTS FILME(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255),
                        ANO INT,
                        DURACAO INT,
                        PAIS VARCHAR(255),
                        DIRETOR VARCHAR(255),
                        AVALIACAO FLOAT)''')


# Implementar classe Filme e realizar o mapeamento da tabela

class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    ano = Column('ANO', Integer)
    duracao = Column('DURACAO', Integer)
    pais = Column('PAIS', String(255))
    diretor = Column('DIRETOR', String(255))
    avaliacao = Column('AVALIACAO', Float)

    def __init__(self, titulo, ano, duracao, pais, diretor, avaliacao):
        self.titulo = titulo
        self.ano = ano
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.avaliacao = avaliacao


# Importar filmes do arquivo de texto movies.txt e inserir no banco de dados

arquivo = open("movies.txt", "r", encoding = "UTF-8")

lista_filme = []
for linha in arquivo:
    lista = linha.split(";")
    filme = Filme(lista[0],int(lista[1]),int(lista[2]),lista[3],lista[4],float(lista[5]))
    lista_filme.append(filme)
session.add_all(lista_filme) 
session.commit()

# Formato do arquivo: 
# titulo;ano;duracao;pais;diretor;avaliacao
# Consultar todos os filmes e ordenar pelo título

result = session.query(Filme).order_by(Filme.titulo)
for i in result:
    print(i.id, i.titulo, i.ano, i.duracao, i.pais, i.diretor, i.avaliacao)

# Consultar filmes do ano de 2020 e ordenar pelo título

result = session.query(Filme).filter(Filme.ano == 2020).order_by(Filme.titulo)
for i in result:
    print(i.id, i.titulo, i.ano, i.duracao, i.pais, i.diretor, i.avaliacao)

# Consultar filmes de 2019 com avaliação superior a 80 e ordenar pelo título

result = session.query(Filme).filter(Filme.ano == 2019 and Filme.avaliacao > 80).order_by(Filme.titulo)
for i in result:
    print(i.id, i.titulo, i.ano, i.duracao, i.pais, i.diretor, i.avaliacao)

# Excluir todos os filmes do ano de 2020

result = session.query(Filme).filter(Filme.ano == 2020)
for i in result:
   session.delete(i)
   session.commit()

# Exportar filmes para um arquivo de texto, ordenados pelo título e no formato:
# título;ano;duracao;país;diretor;avaliacao

arquivo2 = open("movies2.txt", "w", encoding = "UTF-8")

result = session.query(Filme).order_by(Filme.titulo)
for i in result:
    arquivo2.write(f"{i.titulo};{i.ano};{i.duracao};{i.pais};{i.diretor};{i.avaliacao}\n")