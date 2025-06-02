from app.database.connection import Base, engine

def create_tables():
    from app.models import administrador_model, analise_exame_clinico_model, analise_exame_imagem_model, \
    analise_habito_vida_model, analise_medicamento_model, area_model, consulta_model, doencas_model, \
    doencas_prontuario_model, exame_imagem_model, exames_clinicos_model, habitos_vida_model, historico_model, \
    medico_model, medicamento_model, paciente_model, predicao_exame_clinico_model, predicao_exame_imagem_model, \
    predicao_habito_vida_model, predicao_medicamento_model, prontuario_model, secretaria_model, \
    upload_exame_imagem_model, upload_prontuario_model, usuario_model

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