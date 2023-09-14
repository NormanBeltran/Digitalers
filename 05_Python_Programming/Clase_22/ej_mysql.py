"""
Ejercitacion con MYSQL

"""

import pymysql

def conexion():
    try:
        con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "educacionIT",
            db = "peliculas"
        )
    except Exception as e:
        print(f"Ocurrio un error de conexion {e.__class__}")
        return 0
    return con 

def crear_peliculas(con):
    try:
        with con.cursor() as cursor:
            insertar = "INSERT INTO peliculas (nombre, anio) VALUES (%s, %s);"
            cursor.execute(insertar, ("Soy Leyenda", 2007))
            cursor.execute(insertar, ("El libro de Eli", 2010))
            cursor.execute(insertar, ("The Game", 1997))
            cursor.execute(insertar, ("Los otros", 2002))
            cursor.execute(insertar, ("The lord of the rings", 2001))
            cursor.execute(insertar, ("Scarface", 1978))
            cursor.execute(insertar, ("El padrino", 1972))
            con.commit()
    except Exception as e:
        print(f"Fallo el proceso de insert {e.__class__}")    

def consultar_peliculas(con):     
    try:
        with con.cursor() as cursor:             # cursor = con.cursor()
            cursor.execute("SELECT id, nombre, anio FROM peliculas;")
            peliculas = cursor.fetchall()
            for p in peliculas:
                print(p)
    except Exception as e:
        print(f"Hubo un error {e.__class__}, {e.__cause__}")   

def actualizar_pelicula(con, nid, nombre, anio):
    try:
        with con.cursor() as cursor:
            sentencia = "UPDATE peliculas SET nombre = %s, anio = %s WHERE id = %s;"
            cursor.execute(sentencia, (nombre, anio, nid))
            con.commit()
    except Exception as e:
        print(f"Hubo un error {e.__class__}, {e.__cause__}")     

def borrar_pelicula(con, nid):
    try:
        with con.cursor() as cursor:
            cursor.execute("DELETE FROM peliculas WHERE id = %s;", (nid))
            con.commit()
    except Exception as e:
        print(f"Hubo un error {e.__class__}, {e.__cause__}")      

def consultar_filtro(con, buscar):     
    try:
        with con.cursor() as cursor:             # cursor = con.cursor()
            cursor.execute("SELECT id, nombre, anio FROM peliculas WHERE nombre LIKE %s;", ("%{}%".format(buscar)))
            peliculas = cursor.fetchall()
            for p in peliculas:
                print(p)
    except Exception as e:
        print(f"Hubo un error {e.__class__}, {e.__cause__}")       

def consultar_anio(con, nanio):     
    try:
        with con.cursor() as cursor:             # cursor = con.cursor()
            cursor.execute("SELECT id, nombre, anio FROM peliculas WHERE anio > " + str(nanio) + ";")
            peliculas = cursor.fetchall()
            for p in peliculas:
                print(p)
    except Exception as e:
        print(f"Hubo un error {e.__class__}, {e.__cause__}")               
#_______________________________________
conn = conexion()

#crear_peliculas(conn)
#consultar_peliculas(conn)
#actualizar_pelicula(conn, 6, "Rocky", 1976)
#borrar_pelicula(conn, 2)
#consultar_filtro(conn, "The")
consultar_anio(conn, 2000)

conn.close()