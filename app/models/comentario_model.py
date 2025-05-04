from pydantic import BaseModel
import datetime

class comentario(BaseModel):
    id: int = None 
    id_post: int
    id_usuario: int
    contenido: str
    fecha: datetime.datetime = None
