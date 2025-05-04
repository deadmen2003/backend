from fastapi import APIRouter, HTTPException
from controllers.amistades_controller import AmistadControlador
from models.amistades_model import Amistad
from pydantic import BaseModel

router = APIRouter()

amistad_controlador = AmistadControlador()

class SolicitudAmistad(BaseModel):
    usuario_id: int  # ID del usuario que envía la solicitud
    amigo_id: int    # ID del amigo al que se le envía la solicitud

@router.post("/enviar_solicitud_amistad")
async def enviar_solicitud_amistad(solicitud_amistad: SolicitudAmistad):
    amistad = Amistad(usuario_id=solicitud_amistad.usuario_id, amigo_id=solicitud_amistad.amigo_id)
    respuesta = amistad_controlador.crear_solicitud_amistad(amistad)
    return respuesta

@router.post("/aceptar_solicitud_amistad/{amistad_id}")
async def aceptar_solicitud_amistad(amistad_id: int):
    respuesta = amistad_controlador.aceptar_solicitud_amistad(amistad_id=amistad_id)
    return respuesta

@router.get("/obtener_amistades/{usuario_id}")
async def obtener_amistades(usuario_id: int):
    respuesta = amistad_controlador.obtener_amistades(usuario_id=usuario_id)
    return respuesta
