from fastapi import APIRouter, HTTPException
from controllers.bitacora_controller import *
from models.bitacora_model import bitacora

router = APIRouter()

nuevo_seguido = bitacoraController()


@router.post("/create_seguimiento")
async def create_user(bitacora: bitacora):
    rpta = nuevo_seguido.create_seguimiento(bitacora)
    return rpta

@router.get("/get_seguido/{id}",response_model=bitacora)
async def get_seguido(id: int):
    rpta = nuevo_seguido.get_seguido(id)
    return rpta

@router.get("/get_seguidos/")
async def get_seguidos():
    rpta = nuevo_seguido.get_seguidos()
    return rpta

@router.put("/put_seguido/{id}")
async def put_seguido(id:int, bitacora: bitacora):
    rpta = nuevo_seguido.put_seguido(id, bitacora)
    return rpta
