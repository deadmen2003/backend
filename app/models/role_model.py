from pydantic import BaseModel

class role(BaseModel):
    id: int = None
    nombre: str
    descripcion: str