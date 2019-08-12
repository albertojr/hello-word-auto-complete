from django.shortcuts import render
from dal import autocomplete
from .models import Estados
#from django.contrib.auth import authenticate

class EstadoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):#metodo para retornar uma queryset
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated(): (verificar se usuário tem permissão(metodo antigo))
        #https://docs.djangoproject.com/en/2.2/topics/auth/default/
        if not self.request.user.is_authenticated:
            #se o usuário não estiver feito a autenticação, retorna uma lista de objetos vazia
            return Estados.objects.none()

        qs = Estados.objects.all()#se tiver logado, pega todo os objetos de estados

        if self.q:#
            qs = qs.filter(nomeEstado__istartswith=self.q)

        return qs

class LinkedDataView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = super(LinkedDataView, self).get_queryset()
        estado = self.forwarded.get('estado', None)
    
        if estado:
            qs = qs.filter(estados_id=estado)
    
        return qs