from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3

# Create your views here.

def index(request):
    return HttpResponse("¡Hola Mundo!")

def acerca(request):
    return HttpResponse("Mi nombre es ..... soy Ingeniero de Sistemas egresado")

def index2(request):
    html = "<html><strong>Bienvenidos al sitio</strong>  <em>Cursos</em></html>"
    return HttpResponse(html)

def cursos(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    html = """
    <html>
    <title>Listado de Cursos</title>
    <table style='border: 1px solid'>
    <thead>
    <tr>
    <th>Curso</th>
    <th>Inscriptos</th>
    </tr>
    </thead>
    """
    for (nombre, inscriptos) in cursor.fetchall():
        html += f"""
        <tr>
        <td>{nombre}</td>
        <td>{inscriptos}</td>
        </tr>        
        """
    html += "</table></html>"

    conn.close()
    return HttpResponse(html)

def cursos_json(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    response = JsonResponse(cursor.fetchall(), safe=False )
    conn.close()
    return response

def aeropuertos(request):
    f = open("aeropuertos.csv", encoding="utf8")
    html = """
    <html>
    <title>Listado de Aeropuertos</title>
    <table style='border: 1px solid'>
    <thead>
    <tr>
    <th>Aeropuerto</th>
    <th>Ciudad</th>
    <th>Pais</th>
    </tr>
    </thead>
    """    
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"','')
        ciudad = datos[2].replace('"','')
        pais = datos[3].replace('"','')
        html += f"""
        <tr>
        <td>{nombre}</td>
        <td>{ciudad}</td>
        <td>{pais}</td>
        </tr>        
        """
    html += "</table></html>"
    f.close()
    return HttpResponse(html)

def api_aeropuertos(request):
    f = open("aeropuertos.csv", encoding="utf8") 
    aero = []
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"','')
        ciudad = datos[2].replace('"','')
        pais = datos[3].replace('"','')
        d = {"nombre": nombre, "ciudad": ciudad, "pais": pais}
        aero.append(d)
    f.close()
    return JsonResponse(aero, safe=False)