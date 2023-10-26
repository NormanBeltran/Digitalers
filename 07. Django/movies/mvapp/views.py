from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Importaciones de Modelos

from .models import Gender, Company, Movie
from .forms import MovieForm

# Importaciones de CBV

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.views import LoginView

# CLASS BASED VIEWS 

class HomeView(TemplateView):
    template_name = "mvapp/home.html"

class GenderList(ListView):
    model = Gender

class CompanyList(ListView):
    model = Company

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = "Lista de Compañías de Películas"
        return contexto

class MovieList(ListView):
    model = Movie        

class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('peliculas')

class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name_suffix = "_update_form" 

    def get_success_url(self):
        return reverse_lazy('peliculas-actualizar', args=[self.object.id])+"?ok"

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('peliculas')

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña inválidos")
        return self.render_to_response(self.get_context_data(form=form))
