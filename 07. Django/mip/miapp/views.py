from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
import sqlite3
from . import forms 
from .models import Curso, Profesor

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
    # conn = sqlite3.connect("cursos.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT nombre, inscriptos FROM cursos")
    # response = JsonResponse(cursor.fetchall(), safe=False )
    # conn.close()
    response = JsonResponse(list(Curso.objects.values()), safe=False )
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

# ____ Separar codigo HTML de la función Python pero no podemos
#      Integrar datos externos al código HTML

def index3(request):
    f = open("miapp/index.html", encoding="utf-8")
    response = f.read()
    f.close()
    return HttpResponse(response)

# ____ DTL

def index4(request):
    ctx = {
            "nombre": "Juan Pedro Gonzalez",
            "cursos": 5,
            "curso_actual": {"nombre": "Python & Django", "turno": "mañana", "profesor": "Mario Bravo"},
            "cursos_previos": ["Java", "HTML", "CSS", ".Net", "Agile", "Xtreme Programming"]
           }
    return render(request, "miapp/index.html", ctx)

def cursos2(request):     
    cursos = Curso.objects.all()    
    ctx = {"cursos": cursos}
    return render(request, "miapp/cursos.html", ctx)

def curso_nombre(request, nombre_curso):
    # conn = sqlite3.connect("cursos.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT nombre, inscriptos FROM cursos WHERE nombre=?", [nombre_curso])
    # curso = cursor.fetchone()
    # if curso is None:
    #     raise Http404
    
    # conn.close()
    # ctx = {"curso": curso}

    try:
        curso = Curso.objects.get(nombre=nombre_curso)
    except:
        raise Http404
    
    ctx = {"curso": curso}

    return render(request, "miapp/un_curso.html", ctx)


def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)  
        if form.is_valid():
            # form.cleaned_data["nombre"]
            # conn = sqlite3.connect("cursos.db")
            # cursor = conn.cursor()
            # try:
            #     cursor.execute("INSERT INTO cursos VALUES (?,?)", 
            #         (form.cleaned_data["nombre"], form.cleaned_data["inscriptos"]))
            # except:
            #     print("Hubo un error al grabar el curso")                
                
            # conn.commit()
            # conn.close()

            # Curso.objects.create(
            #     nombre=form.cleaned_data["nombre"],
            #     inscriptos=form.cleaned_data["inscriptos"]
            # )
            form.save()
            return HttpResponseRedirect(reverse("cursos2"))  
    else:
        form = forms.FormularioCurso()

    ctx = {"form": form}
    return render(request, "miapp/nuevo_curso.html", ctx)