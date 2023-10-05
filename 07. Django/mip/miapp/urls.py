from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index),
    path('home2/', views.index2),
    path('acerca/', views.acerca),
    path('cursos/', views.cursos),
    path('api_cursos/', views.cursos_json),
    path('aeropuertos/', views.aeropuertos),
    path('api_aeropuertos/', views.api_aeropuertos),
]