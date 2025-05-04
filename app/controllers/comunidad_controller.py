import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from models.comunidad_model import comunidad
from fastapi.encoders import jsonable_encoder

class ComunidadController:
        
    def create_comunidad(self, comunidad: comunidad):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO c.nombre_comunidad, c.activo, u.nombre FROM comunidad c inner join usuarios u on c.nombre = u.id (%s, %s, %s)", (comunidad.nombre_comunidad, comunidad.activo, comunidad.nombre))
            conn.commit()
            conn.close()
            return {"resultado": "Comunidad creada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_comunidad(self, comunidad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comunidad WHERE id = %s", (comunidad_id))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'nombre_comunidad':result[2]
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
       
    def get_comunidades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT c.id, c.nombre_comunidad, c.activo, u.nombre FROM comunidad c inner join usuarios u on c.id_usuario = u.id")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre_comunidad':data[1],
                    'activo':data[2],
                    'nombre':data[3]
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Comunidad not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def put_comunidad(self, comunidad_id: int, comunidad: comunidad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE comunidad SET id_usuario = %s, nombre_comunidad = %s WHERE id = %s", (comunidad.id_usuario, comunidad.nombre_comunidad, comunidad_id))
            conn.commit()
            conn.close()
            return {"resultado": "comunidad editada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_comunidad(self, comunidad_id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM comunidad WHERE id = %s", (comunidad_id))
            conn.commit()
            conn.close()
            return {"resultado": "Comunidad eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()