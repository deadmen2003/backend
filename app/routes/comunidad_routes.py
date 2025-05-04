from fastapi import APIRouter, HTTPException
from app.controllers.comunidad_controller import *
from models.comunidad_model import comunidad

router = APIRouter()

nueva_comunidad = ComunidadController()


@router.post("/create_comunidad")
async def create_comunidad(comunidad: comunidad):
    rpta = nueva_comunidad.create_comunidad(comunidad)
    return rpta

@router.get("/get_comunidad/{comunidad_id}")
async def get_comunidad(comunidad_id: int):
    rpta = nueva_comunidad.get_comunidad(comunidad_id)
    return rpta

@router.get("/get_comunidades/")
async def get_comunidades():
    rpta = nueva_comunidad.get_comunidades()
    return rpta

@router.put("/put_comunidad/{comunidad_id}")
async def put_comunidad(comunidad_id: int, comunidad: comunidad):
    rpta = nueva_comunidad.put_comunidad(comunidad_id, comunidad)
    return rpta

@router.delete("/delete_comunidad/{comunidad_id}")
async def delete_comunidad(comunidad_id: int):
    rpta = nueva_comunidad.delete_user(comunidad_id)
    return rpta