from django.urls import path, include

from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('generos/', GenderList.as_view(), name="generos"),
    path('companias/', CompanyList.as_view(), name="companias"),

    path('peliculas/', MovieList.as_view(), name="peliculas"),
    path('peliculas_crear/', MovieCreate.as_view(), name="peliculas-crear"),
    path('peliculas_actualizar/<int:pk>/', MovieUpdate.as_view(), name="peliculas-actualizar"),
    path('peliculas_eliminar/<int:pk>/', MovieDelete.as_view(), name="peliculas-eliminar"),

    path('login/',  MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
]