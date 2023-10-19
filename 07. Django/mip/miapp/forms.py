from django import forms 
from django.forms import ModelForm
from .models import Curso

from django.core.exceptions import ValidationError

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno")

    # nombre = forms.CharField(label="Nombre", max_length=50)
    # inscriptos = forms.IntegerField(label="Cantidad de Inscriptos")
    # solo_empresas = forms.BooleanField(label="Es solo para empresas?", required=False)
    # TURNOS = (
    #     (1, "Mañana"),
    #     (2, "Tarde"),
    #     (3, "Noche"),
    # )
    # turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    # fecha_inicio = forms.DateField(
    #     label="Fecha Inicio", 
    #     widget=forms.DateInput(attrs={"type": "date"}),
    #     help_text="Ingrese una fecha valida"
    # )
    # mail_coordinador = forms.EmailField(required=True)

    def clean_inscriptos(self):
        inscriptos = self.cleaned_data["inscriptos"]
        if inscriptos > 100:
            raise ValidationError("No se pueden inscribir mas de 100 alumnos")
        return inscriptos