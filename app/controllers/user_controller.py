import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder

class UserController:
        
    def create_user(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (id_role,nombre,apellido,usuario,correo,password) VALUES (%s, %s, %s, %s, %s, %s)", (user.id_role, user.nombre, user.apellido, user.usuario, user.correo, user.password))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        
    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_role':result[1],
                    'nombre':result[2],
                    'apellido':result[3],
                    'usuario':result[4],
                    'estado':result[5],
                    'correo':result[6],
                    'password':result[7],
                    
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
       
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_role':data[1],
                    'nombre':data[2],
                    'apellido':data[3],
                    'usuario':data[4],
                    'estado':data[5],
                    'correo':data[6],
                    'password':data[7],
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

    def put_user(self, user_id: int, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET id_role = %s, nombre = %s, apellido = %s, usuario = %s, estado = %s, correo = %s, password = %s WHERE id = %s", (user.id_role, user.nombre, user.apellido, user.usuario, user.estado, user.correo, user.password, user_id))
            conn.commit()
            conn.close()
            return {"resultado": "usuario editado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            
    def edit_user(self, user_id: int, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET estado = %s WHERE id = %s", (user.estado, user_id))
            conn.commit()
            conn.close()
            return {"resultado": "usuario editado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

