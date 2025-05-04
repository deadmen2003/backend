from pydantic import BaseModel
import datetime

class post(BaseModel):
    id: int = None 
    titulo: str
    contenido: str
    # `fecha` ahora es opcional ya que se genera automáticamente en la base de datos
    fecha: datetime.datetime = None
    id_usuario: int
    id_rol: int
    
