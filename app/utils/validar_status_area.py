from fastapi import HTTPException

VALID_STATUS = ["Ativo", "Inativo"]

def validar_status(status: str):
    if status not in VALID_STATUS:
        raise HTTPException(status_code=400, detail="Status inválido. Use 'Ativo' ou 'Inativo'.")