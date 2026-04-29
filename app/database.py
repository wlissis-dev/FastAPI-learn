from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (estamos usando SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./pokedex.db"

#engine: Prepara a conexão com base na URL.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})

#autocommit=False: Muito importante! 
# Impede que o banco salve alterações automaticamente.
# Você só quer que os dados sejam salvos quando você chamar..
# explicitamente db.commit(). 
# Isso garante segurança em transações.

# autoflush=False: Impede que o banco tente "limpar" a
#  memória enviando comandos automaticamente antes da hora.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base(): Cria a classe da qual seus
# modelos (ex: PokemonORM) irão herdar.
Base= declarative_base()

# Dependency para injetar a sessão do banco em cada requisição da API
# Essa função é o padrão "middleware" do FastAPI.
# db = SessionLocal(): Abre a conexão com o banco.
# yield db: Entrega essa conexão para a sua rota (o main.py). A execução da sua rota pausa aqui.
# finally: db.close(): Crucial! Assim que a rota terminar o trabalho, o banco garante que a conexão seja fechada.
# Sem isso, se muitas pessoas acessarem, você esgota as conexões do banco e o site cai.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()