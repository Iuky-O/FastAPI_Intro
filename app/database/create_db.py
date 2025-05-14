from app.database.connection import Base, engine

def create_tables():
    from app.models import usuario_model
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()