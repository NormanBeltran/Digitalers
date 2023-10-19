from django.contrib import admin
from .models import Gender, Company, Movie

# Register your models here.

class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('pelicula', 'premiere', 'estrellas', 'sinopsis')
    list_filter = ('genders', 'company', 'premiere')
    ordering = ('premiere',)


admin.site.register(Gender, GenderAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Movie, MovieAdmin)