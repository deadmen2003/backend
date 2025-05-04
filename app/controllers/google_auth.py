import requests
from fastapi import HTTPException
from app.config.db_config import get_db_connection
import jwt
from datetime import datetime, timedelta

# Configuración OAuth
CLIENT_ID = "716297006446-dumr7vkjol85v6j00umv3ri9s6o1n3li.apps.googleusercontent.com"
CLIENT_SECRET = "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"
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_google_user(access_token: str):
    """Obtiene los datos del usuario desde Google"""
    response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error al obtener datos del usuario de Google")
    return response.json()

def exchange_code_for_token(code: str, redirect_uri: str):
    """Intercambia el código de autorización por un token de acceso"""
    print(f"Code: {code}")
    print(f"Redirect URI: {redirect_uri}")

    data = {
        "client_id": "716297006446-dumr7vkjol85v6j00umv3ri9s6o1n3li.apps.googleusercontent.com",
        "client_secret": "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",
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
    }

    response = requests.post("https://oauth2.googleapis.com/token", data=data)

    if response.status_code != 200:
        print(f"Error response from Google: {response.text}")
        raise HTTPException(status_code=400, detail="Error al obtener el access_token")

    return response.json()

def login_google_user(code: str, redirect_uri: str):
    """Intercambia el código de Google por un token JWT"""
    # Paso 1: Obtener el access token
    token_data = exchange_code_for_token(code, redirect_uri)
    access_token = token_data.get("access_token")
    
    if not access_token:
        raise HTTPException(status_code=400, detail="No se pudo obtener access_token de Google")
    
    # Paso 2: Obtener los datos del usuario desde Google
    google_user = get_google_user(access_token)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar si el usuario ya está en la base de datos
    cursor.execute("SELECT id, id_role, nombre, apellido, usuario FROM usuarios WHERE usuario = %s", (google_user["email"],))
    user_data = cursor.fetchone()

    if not user_data:
        # Registrar usuario si no existe
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, usuario, password, id_role) VALUES (%s, %s, %s, %s, %s)",
            (google_user["given_name"], google_user["family_name"], google_user["email"], "", 2)  # Asigna un rol por defecto
        )
        conn.commit()
        cursor.execute("SELECT id, id_role, nombre, apellido, usuario FROM usuarios WHERE usuario = %s", (google_user["email"],))
        user_data = cursor.fetchone()

    conn.close()

    user_token = {
        "id": user_data[0],
        "id_role": user_data[1],
        "nombre": user_data[2],
        "apellido": user_data[3],
        "usuario": user_data[4],
    }

    return create_access_token(user_token)
