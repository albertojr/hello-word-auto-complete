from dal import autocomplete
from django import forms
from .models import Estados,Person

class PersonForm(forms.ModelForm):
    def clean_cidade(self):
        estado = self.cleaned_data.get('estado', None)
        cidade = self.cleaned_data.get('cidade', None)

        # if value and owner and value.owner != owner:
        #     raise forms.ValidationError('Wrong owner for test')

        return cidade

    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {
            'cidade': autocomplete.ModelSelect2(url='linked_data',
                                              forward=('estado',))
        }
        
    class Media:
        js = (
            'linked_data.js',
        )

    # class Meta:
    #     model = Person
    #     fields = ('__all__')
    #     widgets = {
    #         'estado': autocomplete.ModelSelect2(url='estados-autocomplete')
    #     }