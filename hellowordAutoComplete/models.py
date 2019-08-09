from django.db import models
#from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class Estados(models.Model):
    idEstado = models.AutoField(primary_key=True)
    nomeEstado = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeEstado

    class meta:
        ordering = ['nomeEstado']
        verbose_name_plural = "Estados"
        db_table = 'Estados'

class Person(models.Model):
    idPerson = models.AutoField(primary_key=True)
    nomePerson = models.CharField(max_length=100)
    idade = models.IntegerField()
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nomePerson

    class Meta:
        ordering = ["nomePerson"]
        verbose_name_plural = "Pessoas"
        db_table = 'Pessoas'