import os
import shutil
from uuid import uuid4
from fastapi import UploadFile

def salvar_arquivo_upload(file: UploadFile, upload_dir: str) -> str:
    ext = file.filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    filepath = os.path.join(upload_dir, filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return filename
