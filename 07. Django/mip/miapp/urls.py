from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('home2/', views.index2, name="home2"),
    path('home3/', views.index3, name="home3"),
    path('home4/', views.index4, name="home4"),
    
    path('acerca/', views.acerca, name="acerca"),

    path('cursos/', views.cursos, name="cursos"),
    path('cursos2/', views.cursos2, name="cursos2"),
    path('curso/<str:nombre_curso>/', views.curso_nombre, name="un_curso"),

    path('api_cursos/', views.cursos_json, name="api"),
    path('lista_aeropuertos/', views.aeropuertos, name="aeropuertos"),
    path('api_aeropuertos/', views.api_aeropuertos, name="api_aeropuertos"),
]