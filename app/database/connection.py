# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from app.config import DATABASE_URL

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def create_tables():
#     from app.models import usuario_model  # Importa para registrar no Base
#     Base.metadata.create_all(bind=engine)