#cria a conexão com o banco de dados.
#sessionmaker cria sessões para fazer consultas (CRUD) no banco. | declarative_base é usada para criar a base das models

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()