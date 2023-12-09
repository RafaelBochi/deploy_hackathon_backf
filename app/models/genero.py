from django.db import models

class Genero(models.Model):
    name = models.CharField(max_length=100)
    qntLivros = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name