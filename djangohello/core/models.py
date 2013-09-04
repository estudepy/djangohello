from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    
    def __unicode__(self):
        return '%s - %s' % (self.nome, self.cpf)
