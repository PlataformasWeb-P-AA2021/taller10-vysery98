from django import forms
from django.forms import ModelForm
from ordenamiento.models import Parroquia, Barrio

class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo_parroquia'] 

class BarrioParroquiaForm(ModelForm): 
    
    def __init__(self, nombre, *args, **kwargs):    
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)       
        self.initial['parroquia'] = nombre
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(nombre)
    
    class Meta:
        model = Barrio
        fields = ['nombre','viviendas','parques', 'edificios', 'parroquia']

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre','viviendas','parques', 'edificios', 'parroquia']

