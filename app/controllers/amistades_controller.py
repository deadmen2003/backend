import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.amistades_model import Amistad
from models.user_model import User
from fastapi.encoders import jsonable_encoder

class AmistadControlador:

    def crear_solicitud_amistad(self, amistad: Amistad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO amistades (usuario_id, amigo_id, estado) VALUES (%s, %s, %s)", 
                (amistad.usuario_id, amistad.amigo_id, amistad.estado)
            )
            conn.commit()
            return {"resultado": "Solicitud de amistad enviada"}
        except mysql.connector.Error as err:
            print(f"Error: {err}")  # Imprimir error para debug
            raise HTTPException(status_code=500, detail="Error al enviar solicitud de amistad")
        finally:
            if conn.is_connected():
                conn.close()

    def aceptar_solicitud_amistad(self, amistad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE amistades SET estado = %s WHERE id = %s", 
                ("aceptada", amistad_id)
            )
            conn.commit()
            return {"resultado": "Solicitud de amistad aceptada"}
        except mysql.connector.Error as err:
            print(f"Error: {err}")  # Imprimir error para debug
            raise HTTPException(status_code=500, detail="Error al aceptar solicitud de amistad")
        finally:
            if conn.is_connected():
                conn.close()

    def obtener_amistades(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM amistades WHERE usuario_id = %s OR amigo_id = %s", (usuario_id, usuario_id))
            resultado = cursor.fetchall()
            amistades = []
            for registro in resultado:
                amistad = {
                    'id': registro[0],
                    'usuario_id': registro[1],
                    'amigo_id': registro[2],
                    'estado': registro[3],
                    'fecha': registro[4],  # Incluye la fecha
                }
                amistades.append(amistad)
            return {"resultado": amistades}
        except mysql.connector.Error as err:
            print(f"Error: {err}")  # Imprimir error para debug
            raise HTTPException(status_code=500, detail="Error al obtener amistades")
        finally:
            if conn.is_connected():
                conn.close()