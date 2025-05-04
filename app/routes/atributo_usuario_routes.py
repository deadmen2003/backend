from fastapi import APIRouter, HTTPException
from app.controllers.atributo_usuario_controller import *
from models.user_model import User

router = APIRouter()

nuevo_atxus = atxusController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_atxus.create_user(user)
    return rpta


@router.get("/get_user/{atxus_id}",response_model=User)
async def get_user(user_id: int):
    rpta = nuevo_atxus.get_atxus(atxus_id)
    return rpta

@router.get("/get_users/")
async def get_users():
    rpta = nuevo_atxus.get_users()
    return rpta

@router.delete("/delete_atxus/{atxus_id}",response_model=User)
async def delete_user(user_id: int):
    rpta = nuevo_atxus.delete_atxus(atxus_id)
    return rpta

@router.put("/put_user/{atxus_id}")
async def put_user(user_id:int, User:User):
    rpta = nuevo_atxus.edit_atxus(atxus_id, atxus)
    return rpta
