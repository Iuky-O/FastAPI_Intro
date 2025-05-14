"""from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from app.config import settings

engine = create_engine(settings.db.uri, connect_args=settings.db.connect_args)

try:
    with engine.connect() as conn:
        print("Conexão com o banco de dados bem-sucedida!")
except OperationalError as e:
    print("Falha na conexão com o banco de dados:")
    print(e)"""