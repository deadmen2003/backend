import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.atributo_usuario_model import atxus
from fastapi.encoders import jsonable_encoder

class atxusController:

#Crear usuario        
    def create_user(self, atxus: atxus):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (id_usuario,id_rol,valor,descripcion) VALUES (%s, %s, %s ,%s)", (atxus.nombre, atxus.apellido, atxus.usuario, atxus.correo, atxus.password))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

#Ver usuario
    def get_user(self, atxus_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (atxus_id))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'apellido':result[2],
                    'usuario':result[3],
                    'correo':result[4],
                    'password':result[5]
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
       

#Ver Usuarios
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
                    'nombre':data[1],
                    'apellido':data[2],
                    'usuario':data[3],
                    'correo':data[4],
                    'password':data[5],
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

#Borrar usuario
    def delete_user(atxus_id:int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def put_user(atxus_id:int, atxus:atxus):
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE * FROM usuarios SET (nombre,apellido,usuario,correo,password) VALUES (%s, %s, %s, %s ,%s)", (user.nombre, user.apellido, user.usuario, user.correo, user.password))
                conn.commit()
                conn.close()
                return {"resultado": "Usuario actualizado"}
            except mysql.connector.Error as err:
                conn.rollback()
            finally:
                conn.close()
    
       

##user_controller = UserController()