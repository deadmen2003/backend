from pydantic import BaseModel
import datetime

class bitacora(BaseModel):
    id: int = None
    id_usuario: int 
    id_rol: int
    id_paciente: int
    mensaje: str
    fecha: datetime.datetime = None
    cerrar: str = None
