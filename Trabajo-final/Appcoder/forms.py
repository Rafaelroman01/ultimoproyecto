from django import forms


class RecreadorFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    nacimiento = forms.DateField()
    
class ParticipanteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    nacimiento = forms.DateField()
    
class ExcursionFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField() 
    
   
    