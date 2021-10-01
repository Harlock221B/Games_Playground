from django.db import models
from django.utils import timezone

class Produtora(models.Model):
        name = models.CharField(max_length=60)
        description = models.CharField(max_length=200)
        logo = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')
        def __str__(self):
                return self.name

class Games(models.Model):
        title = models.CharField(max_length=60)
        description = models.CharField(max_length=500)
        lancamento = models.DateTimeField(default=timezone.now())
        mostrar = models.BooleanField(default=True)
        produtora = models.ForeignKey(Produtora, on_delete=models.DO_NOTHING)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        gender = models.CharField(max_length=10,default='A',choices=(('A','Multiplayer'),('B','Single-Player'),('C','MMO')))
        foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')

        def __str__(self):
                return self.title