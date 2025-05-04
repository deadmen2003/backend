from pydantic import BaseModel
from datetime import datetime

class amigos(BaseModel):
    id: int = None 
    id_envio: int
    id_receptor: int
    aceptar: str
    fecha_soli: datetime
