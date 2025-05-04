from pydantic import BaseModel

# Modelo Pydantic para recibir los datos del usuario

class contacto(BaseModel):
    id: int = None
    nombre: str
    correo: str
    telefono: str
    mensaje: str
