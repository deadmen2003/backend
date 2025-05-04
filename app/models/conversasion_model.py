from pydantic import BaseModel
from datetime import datetime

class conversacion(BaseModel):
    id: int = None 
    id_uenvio: int
    id_ureceptor: int
    fecha: datetime
