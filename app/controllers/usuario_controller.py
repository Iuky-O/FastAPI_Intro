# from sqlalchemy.orm import Session
# from app.models.usuario_model import Usuario
# from app.schemas.usuario_schema import UsuarioCreate

# def criar_usuario(db: Session, usuario: UsuarioCreate):
#     novo_usuario = Usuario(**usuario.dict())
#     db.add(novo_usuario)
#     db.commit()
#     db.refresh(novo_usuario)
#     return novo_usuario

# def listar_usuarios(db: Session):
#     return db.query(Usuario).all()
