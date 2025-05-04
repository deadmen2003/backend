from pydantic import BaseModel

class atributo(BaseModel):
    id_usuario: int
    id_rol: int
    activo: str
    creacion: str
    id_comunidad: int
    genero: str