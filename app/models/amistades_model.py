from pydantic import BaseModel
import datetime

# Modelo Pydantic para los datos de amistad
class Amistad(BaseModel):
    id: int = None
    usuario_id: int    # ID del usuario que envía la solicitud
    amigo_id: int      # ID del usuario que recibe la solicitud
    estado: str = "pendiente"  # Estado de la solicitud: "pendiente", "aceptada" o "rechazada"
    fecha: datetime.datetime = None 