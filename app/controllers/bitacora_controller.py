import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from models.bitacora_model import bitacora
from fastapi.encoders import jsonable_encoder

class bitacoraController:
        
    def create_seguimiento(self, bitacora: bitacora):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bitacora (id_usuario,id_rol,id_paciente,mensaje) VALUES (%s, %s, %s, %s)", (bitacora.id_usuario, bitacora.id_rol, bitacora.id_paciente, bitacora.mensaje))
            conn.commit()
            conn.close()
            return {"resultado": "mensaje creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        
    def get_seguido(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bitacora WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':result[1],
                    'id_rol':result[2],
                    'id_paciente':result[3],
                    'mensaje':result[4],
                    'fecha':result[5],
                    'cerrar':result[6],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_seguidos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bitacora")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'id_rol':data[2],
                    'id_paciente':data[3],
                    'mensaje':data[4],
                    'fecha':data[5],
                    'cerrar':data[6],
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

    def put_seguido(self, id: int, bitacora: bitacora):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE bitacora SET id_usuario = %s, id_rol = %s, id_paciente = %s, mensaje = %s, cerrar = %s WHERE id = %s", (bitacora.id_usuario, bitacora.id_rol, bitacora.id_paciente, bitacora.mensaje, bitacora.cerrar, id))
            conn.commit()
            conn.close()
            return {"resultado": "datos editados"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
