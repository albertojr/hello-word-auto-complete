from django.contrib import admin
from .models import Person,Estados
from .forms import PersonForm


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm


admin.site.register(Person,PersonAdmin)
admin.site.register(Estados)