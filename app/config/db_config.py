
import mysql.connector

# Configuración de la conexión a la base de datos

def get_db_connection():
    return mysql.connector.connect(
        host="b6tvokx7ldxdr41mw8vn-mysql.services.clever-cloud.com",
        user="uaizbfpuehbnj5s5",
        password="bR8Tz3MkrnaMonhZRkkH",
        database="b6tvokx7ldxdr41mw8vn"
    )

"""import mysql.connector


# Configuración de la conexión a la base de datos

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="red_social"
    )"""
