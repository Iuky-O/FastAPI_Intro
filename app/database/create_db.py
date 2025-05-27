from app.database.connection import Base, engine

def create_tables():
    from app.models import usuario_model, medico_model, secretaria_model, area_model, administrador_model
    print("Criando as tabelas...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas.")

if __name__ == "__main__":
    create_tables()

# import asyncio
# from app.database.connection import engine
# from app.database.connection import Base

# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)