import random
from django.db import models

def gereador_codigo(size=6, chars='abcderfghijklmnopqrstuvwxyz'):
    codigo_novo=''
    for _ in range(size):
        codigo_novo += random.choice(chars)
    return ''.join(random.choice(chars) for _ in range(size))

class testeURLManager(models.Manager):
    def todos(self, *args, **kwargs):
        qs = super(testeURLManager, self).all(*args, **kwargs)
        return qs
    
class testeURL(models.Model):
    url = models.CharField(max_length=220, )


    def salvar(self, *args, **kwargs):
        super(testeURL, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.url)
    
    def __unicode__(self):
        return str(self.url)
