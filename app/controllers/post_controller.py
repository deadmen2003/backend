import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.post_model import post
from fastapi.encoders import jsonable_encoder

class postController:
        
    def create_post(self, post: post):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO post (titulo, contenido, id_usuario, id_rol) VALUES (%s, %s, %s, %s)",
                (post.titulo, post.contenido, post.id_usuario, post.id_rol)
            )
            conn.commit()

            nuevo_id = cursor.lastrowid 

            if not nuevo_id:
                raise HTTPException(status_code=500, detail="No se pudo obtener el ID del post")

            return {"id": nuevo_id, "resultado": "Post creado"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(err)}")

        finally:
            conn.close()
        

    def get_post(self, post_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM post WHERE id = %s", (post_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'titulo':result[1],
                    'contenido':result[2],
                    'fecha':result[3],
                    'id_usuario':result[4],
                    'id_rol':result[5],
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
       
    def get_posts(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM post")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'titulo':data[1],
                    'contenido':data[2],
                    'fecha':data[3],
                    'id_usuario':data[4],
                    'id_rol':data[5],
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

    def put_post(self, id: int, post: post):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE post SET titulo = %s, contenido = %s, fecha = %s, id_usuario = %s, id_rol = %s WHERE id = %s", (post.titulo, post. contenido, post.fecha, post.id_usuario, post.id_rol, id))
            conn.commit()
            conn.close()
            return {"resultado": "post editado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_post(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM post WHERE id = %s", (id))
            conn.commit()
            conn.close()
            return {"resultado": "Post eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    