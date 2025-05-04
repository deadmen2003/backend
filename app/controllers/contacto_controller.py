import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from models.contacto_model import contacto
from fastapi.encoders import jsonable_encoder

class ContactoController:
        
    def create_contacto(self, contacto: contacto):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contacto (nombre,correo,telefono,mensaje) VALUES (%s, %s, %s, %s)", (contacto.nombre, contacto.correo, contacto.telefono, contacto.mensaje))
            conn.commit()
            conn.close()
            return {"resultado": "Contacto creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_contactos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacto")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'correo':data[2],
                    'telefono':data[3],
                    'mensaje':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()