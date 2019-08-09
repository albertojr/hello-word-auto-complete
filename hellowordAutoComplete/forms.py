from dal import autocomplete
from django import forms
from .models import Estados,Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {
            'estado': autocomplete.ModelSelect2(url='estados-autocomplete')
        }