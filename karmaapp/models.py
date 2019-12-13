from django.db import models

# Create your models here.
class Espumado(models.Model):
	fecha_producido = models.CharField(max_length=200)

class Meta:
    abstract = True

    def __str__(self):
        return 'fecha_producido: {0} '   .format(self.fecha_producido)


class Block(Espumado):
    pass

class Cilindro(Espumado):
    pass