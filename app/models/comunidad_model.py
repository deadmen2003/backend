from pydantic import BaseModel

# Modelo Pydantic para recibir los datos del comunidad

class comunidad(BaseModel):
    id: int = None
    id_usuario: int
    nombre_comunidad: str
    activo: str
