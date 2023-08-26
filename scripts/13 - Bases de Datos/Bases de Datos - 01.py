#TEMA: Creacion de una tabla

#################################################################
import sqlite3
#################################################################


#################################################################
#Creamos base de datos y conexion
#Si la base de datos existe solo debemos conectarnos
mi_conexion= sqlite3.connect("Primera_base")

#Creamos el cursor o puntero
mi_cursor = mi_conexion.cursor()

#Creamos una tabla
mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


#Confirmamos los cambios
mi_conexion.commit()

#Cerramos el cursor o puntero

#Cerramos la conexion
mi_conexion.close()
#################################################################