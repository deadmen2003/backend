from pydantic import BaseModel
from datetime import datetime

class mensaje(BaseModel):
    id: int = None 
    contenido: str
    id_usuario: int
    id_conversacion: int
    fecha: datetime