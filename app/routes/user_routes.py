from fastapi import APIRouter, HTTPException
from app.controllers.user_controller import *
from models.user_model import User
from utils import send_email

router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    if "error" in rpta:
        raise HTTPException(status_code=400, detail=rpta["error"])

    # Contenido del correo de bienvenida
    subject = "Bienvenido a nuestra plataforma"
    body = f"""
    <html>
        <body>
            <h2>¡Hola, {user.usuario}!</h2>
            <p>Tu cuenta ha sido creada exitosamente.</p>
            <p>Puedes iniciar sesión con tu usuario: {user.usuario} Y la contraseña que asignaste</p>
            <br>
            <p>Saludos,<br>El equipo de soporte</p>
        </body>
    </html>
    """
    
    email_response = send_email(user.correo, subject, body)

    return {
        "message": "Usuario registrado correctamente, se ha enviado un correo de confirmación.",
        "email_status": email_response
    }

@router.get("/get_user/{user_id}",response_model=User)
async def get_user(user_id: int):
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_users/")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta

@router.put("/put_user/{user_id}")
async def put_user(user_id:int, user: User):
    rpta = nuevo_usuario.put_user(user_id, user)
    return rpta

@router.put("/edit_user/{user_id}")
async def edit_user(user_id:int, user: User):
    rpta = nuevo_usuario.edit_user(user_id, user)
    return rpta

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    rpta = nuevo_usuario.delete_user(user_id)
    return rpta