from fastapi import APIRouter, HTTPException
from controllers.comentario_controller import comentarioController
from typing import List
from models.comentario_model import comentario

router = APIRouter()
nuevo_comentario = comentarioController()

@router.post("/create_comentario")
async def create_comentario(comentario: comentario):
    rpta = nuevo_comentario.create_comentario(comentario)
    return rpta

@router.get("/get_comentario/{id_post}", response_model=List[comentario])
async def get_comentario(id_post: int):
    rpta = nuevo_comentario.get_comentario(id_post)
    return rpta

@router.get("/get_comentarios/")
async def get_comentarios():
    rpta = nuevo_comentario.get_comentarios()
    return rpta

@router.put("/put_comentario/{id}")
async def put_comentario(id: int, comentario: comentario):
    rpta = nuevo_comentario.put_comentario(id, comentario)
    return rpta

@router.delete("/delete_comentario/{id}")
async def delete_comentario(id: int):
    rpta = nuevo_comentario.delete_comentario(id)
    return rpta
