from django.db import models


class Tipo_de_espuma(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    modelo = models.CharField(max_length =100)
    especial = models.BooleanField()
    linea = models.BooleanField()
    def __str__(self):
        return self.modelo  

class Ajuste(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    ajuste = models.CharField(max_length = 200)
    def __str__(self):
        return self.ajuste


class Tipo_de_unidad(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    tipo_de_unidad = models.CharField(max_length = 100)
    def __str__(self):
        return self.tipo_de_unidad


class Defecto(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    nombre_de_defecto = models.CharField(max_length =100)
    puntuacion_de_defecto = models.IntegerField('puntuacion del defecto')
    imagen_tipo_defecto =models.CharField(max_length = 500,default="https://pbs.twimg.com/profile_images/1096162188635496449/3hAeJOKz_400x400.png ")
    

    def __str__(self):
        return 'nombre de defecto: {0} | puntuacion de defecto: {1}  '   .format(self.nombre_de_defecto, self.puntuacion_de_defecto,)


class Cliente(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    nombre_de_cliente = models.CharField(max_length = 200)
    tolerancia = models.IntegerField('Tolerancia del defecto')
    def __str__(self):
        return 'nombre de Cliente: {0} | puntuacion de Tolerancia: {1}  '   .format(self.nombre_de_cliente, self.tolerancia,)



class Espumado(models.Model):
	fecha_producido = models.DateTimeField(auto_now_add=True)

class Meta:
    abstract = True

    def __str__(self):
        return 'fecha_producido: {0} '   .format(self.fecha_producido)


class Cilindro(Espumado):
    pass

class Block(Espumado):
    pass