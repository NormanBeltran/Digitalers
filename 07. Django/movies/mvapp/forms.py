from django import forms
from .models import Movie
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'description', 'rating', 'genders', 'company', 'image', 'premiere' ]
        RATING = [
            (1, "Mala"),
            (2, "Mediocre"),
            (3, "Buena"),
            (4, "Muy Buena"),
            (5, "Excelente")
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Película'}),
            'description': CKEditorWidget(),
            'rating': forms.Select(attrs={'class':'form-control', 'placeholder':'Rating'}),
            'genders': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Géneros'}),
            'company': forms.Select(attrs={'class':'form-control', 'placeholder':'Compañía'}),
            'premiere': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Año Estreno'}),
        }

        labels = {
            'name': "",
            'description': ""
        }

    def clean_premiere(self):
        anio = self.cleaned_data['premiere']
        if anio < 1920:
            raise ValidationError(("Error: No existian peliculas sonoras antes de 1920"))
        return anio