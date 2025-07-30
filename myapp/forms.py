from django import forms
from .models import SOSrefugio


class AmigoForm(forms.Form):
     nombre = forms.CharField()
     fecha_nacimiento_estimada = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
     especie = forms.CharField()
     descripcion = forms.CharField(widget=forms.Textarea, required=False)
     email = forms.EmailField() 

class TransitadorForm(forms.Form):
     nombre = forms.CharField(max_length=100)
     sobre_mi_hogar = forms.CharField(widget=forms.Textarea, required=False)
     email = forms.EmailField()

class DonacionForm(forms.Form):
     nombre = forms.CharField(max_length=100)
     objeto_a_donar = forms.CharField(max_length=200)
     punto_de_encuentro = forms.CharField(max_length=180)
     dia_hora_preferencia = forms.CharField(max_length=150)
     email = forms.EmailField()
          


# class TutorForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=100)
#     email = forms.EmailField()

class SOSrefugioForm(forms.ModelForm):
     class Meta:
          model = SOSrefugio
          fields = ['nombre', 'objeto_solicitado', 'punto_de_encuentro', 'dia_hora_preferencia', 'email']
