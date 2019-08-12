from django.contrib import admin
from .models import Person,Estados,Cidade
from .forms import PersonForm


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm


admin.site.register(Person,PersonAdmin)
admin.site.register(Estados)
admin.site.register(Cidade)