from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

DATABASE_URL=settings.db.uri

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from app.config import settings

# print("Ambiente ativo:", settings.current_env)
# print("DB URI:", settings.db.uri)
# DATABASE_URL = settings.db.uri

# # Async engine
# engine = create_async_engine(DATABASE_URL, echo=True)

# # Async session
# async_session = sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False
# )

# # Declarative Base
# Base = declarative_base()

# # Dependency para FastAPI
# async def get_async_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session
