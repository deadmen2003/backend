from pydantic import BaseModel

class atxus(BaseModel):
    id: int = None 
    id_usuario: int
    id_rol: int
    valor: str
    descripcion: str