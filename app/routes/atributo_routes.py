from fastapi import APIRouter, HTTPException
from controllers.atributo_controller import *
from models.atributo_model import atributo

router = APIRouter()

nuevo_atributo = atributoController()


@router.post("/create_atributo")
async def create_atributo(atributo: atributo):
    rpta = nuevo_atributo.create_atributo(atributo)
    return rpta


@router.get("/get_atributo/{user_id}",response_model=atributo)
async def get_user(user_id: int):
    rpta = nuevo_atributo.get_user(user_id)
    return rpta

@router.get("/get_atributos/")
async def get_atributos():
    rpta = nuevo_atributo.get_atrobutos()
    return rpta