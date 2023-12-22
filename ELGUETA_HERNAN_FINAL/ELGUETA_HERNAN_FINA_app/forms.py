from django import forms
from ELGUETA_HERNAN_FINA_app.models import Institucion 

class RegistroInstitucion(forms.Form):

    ESTADOS = [('reservado', 'RESERVADO'),('completada','COMPLETADA'), ('anulada','ANULADA'),('no asisten','NO ASISTEN')]

    nombre = forms.CharField()
    telefono = forms.CharField()
    fecha = forms.DateField()
    hora = forms.TimeField()
    institucion = forms.CharField()
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    

    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fecha.widget.attrs['class'] = 'form-control'
    hora.widget.attrs['class'] = 'form-control'
    institucion.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class']= 'form-select'

class agregar_institucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'