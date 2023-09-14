"""
Ejercitacion con SQLite3

"""

import sqlite3
#__________________________________________________

def crear_tabla():
    cursor.execute("""
        CREATE TABLE empleados (
                id              integer PRIMARY KEY,
                nombre          text,
                salario         real,
                departamento    text,
                posicion        text,
                fecha_ingreso   text,
                edad            numeric
        )
    """
    )

def insertar_datos():
    personas =(
        (1, "Jose Perez", 500000, "Finanzas", "Jefe", "2010-01-01", 45),
        (2, "Antonia Gomez", 600000, "RRHH", "Recruiter", "2012-01-01", 35),
        (3, "Pedro Picapiedra", 700000, "IT", "Programador Python", "2015-01-01", 25),
        (4, "Maria Perez", 550000, "Tesoreria", "Director", "2004-01-01", 41),
        (5, "Marta Perez", 560000, "Operaciones", "Ayudante", "2009-01-01", 55),
        (6, "Juan Perez", 570000, "Logistica", "Supervisor", "2008-01-01", 21),
    )    

    for nid, nombre, salario, depto, posicion, fingreso, edad in personas:
        cursor.execute("INSERT INTO empleados VALUES (?,?,?,?,?,?,?)", 
                       (nid, nombre, salario, depto, posicion, fingreso, edad))
    conn.commit()

def consultar_datos():
    cursor.execute("SELECT * FROM empleados")    
    filas = cursor.fetchall()
    print("Listado de empleados de la empresa")
    print("-"*60)
    for f in filas:
        print(f)

def consultar_uno(nid):
    cursor.execute("SELECT * FROM empleados WHERE id=" + str(nid))    
    fila = cursor.fetchone()
    print(fila)

def consultar_filtro(buscar):
    cursor.execute(f'SELECT * FROM empleados WHERE nombre LIKE "%{buscar}%" ;')    
    filas = cursor.fetchall()
    print(f"Listado de empleados de la empresa con {buscar}")
    print("-"*60)
    for f in filas:
        print(f)

def actualizar_datos(nid, nposicion):
    cursor.execute("UPDATE empleados SET posicion = ? WHERE id = ?", 
                       (nposicion, nid))
    conn.commit()


def borrar_uno(nid):
    cursor.execute("DELETE FROM empleados WHERE id = " + str(nid))
    conn.commit()    
#__________________________________________________
conn = sqlite3.connect("empleados.db")

cursor = conn.cursor()

#crear_tabla()
#insertar_datos()
#consultar_datos()
#consultar_uno(3)
#consultar_filtro("Perez")
#actualizar_datos(3, "Director de Desarrollo")
#consultar_uno(3)
borrar_uno(2)
consultar_datos()

conn.close()