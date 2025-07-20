from django import forms


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
          


# class TutorForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=100)
#     email = forms.EmailField()
