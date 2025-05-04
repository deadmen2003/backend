from pydantic import BaseModel

class pais(BaseModel):
    id: int = None 
    nombre: str
    prefijo: str