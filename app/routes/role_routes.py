from fastapi import APIRouter, HTTPException
from controllers.role_controller import *
from models.role_model import role

router = APIRouter()

nuevo_role = roleController()

@router.post("/create_role")
async def create_role(role: role):
    rpta = nuevo_role.create_role(role)
    return rpta

@router.get("/get_role/{id}",response_model=role)
async def get_role(id: int):
    rpta = nuevo_role.get_role(id)
    return rpta

@router.get("/get_roles/")
async def get_roles():
    rpta = nuevo_role.get_roles()
    return rpta

@router.put("/edit_role/{role_id}")
async def put_role(role_id: int, role: role):
    rpta = nuevo_role.put_role(role_id, role)
    return rpta

# @router.delete("/delete_role/{id}",response_model=role)
# async def get_role(id: int):
#     rpta = nuevo_role.get_role(id)
#     return rpta
