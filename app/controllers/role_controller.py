import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.role_model import role
from fastapi.encoders import jsonable_encoder

class roleController:
        
    def create_role(self, role: role):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO role (nombre,descripcion) VALUES (%s, %s)", (role.nombre, role.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_role(self, role_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM role WHERE id = %s", (role_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
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
       
    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM role")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
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
    
    def put_role(self, role_id: int, role: role):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE role SET nombre = %s, descripcion = %s WHERE id = %s", (role.nombre, role.descripcion, role_id))
            conn.commit()
            conn.close()
            return {"resultado": "rol editado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
