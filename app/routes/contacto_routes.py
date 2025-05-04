from fastapi import APIRouter, HTTPException
from controllers.contacto_controller import *
from models.contacto_model import contacto

router = APIRouter()

nuevo_contacto = ContactoController()


@router.post("/create_contacto")
async def create_contacto(contacto: contacto):
    rpta = nuevo_contacto.create_contacto(contacto)
    return rpta

@router.get("/get_contactos/")
async def get_contactos():
    rpta = nuevo_contacto.get_contactos()
    return rpta