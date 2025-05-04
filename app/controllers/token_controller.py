import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.token_model import Auth
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

class AuthController:
        
    def login(self, auth: Auth):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Obtener usuario y contraseña
            cursor.execute("SELECT id, id_role, nombre, apellido, usuario, password FROM usuarios WHERE usuario = %s", (auth.usuario,))
            user_data = cursor.fetchone()
            conn.close()

            if user_data and auth.password == user_data[5]:  # Verifica la contraseña
                user_token = { 
                    "id": user_data[0],
                    "id_role": user_data[1],
                    "nombre": user_data[2],
                    "apellido": user_data[3],
                    "usuario": user_data[4],
                }
                return user_token

            return None  # Usuario o contraseña incorrectos

        except mysql.connector.Error:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error en la base de datos")

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def validate_token(self, token, output=True):
        try:
            if output:
                return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.exceptions.DecodeError:
            return JSONResponse(content={"mensaje": "Token inválido"}, status_code=401)
        except jwt.exceptions.ExpiredSignatureError:
            return JSONResponse(content={"mensaje": "Token expirado"}, status_code=401)
