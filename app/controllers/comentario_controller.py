import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.comentario_model import comentario
from fastapi.encoders import jsonable_encoder

class comentarioController:
        
    def create_comentario(self, comentario: comentario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = "INSERT INTO comentario (id_post, id_usuario, contenido) VALUES (%s, %s, %s)"
            values = (comentario.id_post, comentario.id_usuario, comentario.contenido)
            cursor.execute(query, values)
            conn.commit()

            nuevo_id = cursor.lastrowid  # 🔥 Obtener el ID del nuevo comentario

            if not nuevo_id:
                raise HTTPException(status_code=500, detail="No se pudo obtener el ID del comentario")

            return {"id": nuevo_id, "resultado": "Comentario creado"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(err)}")

        finally:
            conn.close()

    def get_comentario(self, id_post: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comentario WHERE id_post = %s", (id_post,))
            result = cursor.fetchall()  
            
            if not result:
                raise HTTPException(status_code=404, detail="No comments found for this post")

            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'id_post': data[1],
                    'id_usuario': data[2],
                    'contenido': data[3],
                    'fecha': data[4]
                }
                payload.append(content)

            return jsonable_encoder(payload)  

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(err)}")
        finally:
            conn.close()

    def get_comentarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comentario")
            result = cursor.fetchall()
            payload = []
            
            for data in result:
                content = {
                    'id': data[0],
                    'id_post': data[1],
                    'id_usuario': data[2],
                    'contenido': data[3],
                    'fecha': data[4]
                }
                payload.append(content)

            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No comments found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(err)}")
        finally:
            conn.close()

    def put_comentario(self, id: int, comentario: comentario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "UPDATE comentario SET id_post = %s, id_usuario = %s, contenido = %s, fecha = %s WHERE id = %s"
            values = (comentario.id_post, comentario.id_usuario, comentario.contenido, comentario.fecha, id)
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Comentario no encontrado")

            return {"resultado": "Comentario editado"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(err)}")
        finally:
            conn.close()

    def delete_comentario(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM comentario WHERE id = %s", (id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Comentario no encontrado")

            return {"resultado": "Comentario eliminado"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(err)}")
        finally:
            conn.close()
