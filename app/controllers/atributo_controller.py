import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from models.atributo_model import atributo
from fastapi.encoders import jsonable_encoder

class atributoController:
        
    def create_role(self, atributo: atributo):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atributo (activo,creacion,genero) VALUES (%s, %s, %s)", (atributo.activo, atributo.creacion, atributo.genero))
            conn.commit()
            conn.close()
            return {"resultado": "atributo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_role(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo WHERE id = %s", (id))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'activo':int(result[0]),
                    'creacion':result[1],
                    'genero':result[2],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="atributo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'activo':data[0],
                    'creacion':data[1],
                    'genero':data[2],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="atributo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_atributo(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE * FROM atributo WHERE id = %s", (id))
            conn.commit()
            conn.close()
            return {"resultado": "atributo eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()