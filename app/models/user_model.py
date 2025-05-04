from pydantic import BaseModel

# Modelo Pydantic para recibir los datos del usuario

class User(BaseModel):
    id: int = None
    id_role: int 
    nombre: str
    apellido: str
    usuario: str
    estado: int
    correo: str
    password: str
