from django.db import models
# from model_utils import Choices





CATEGORIA_CHOICES = ( 
    ("linea", "linea"), 
    ("especial", "especial"), 
    
) 
  
# declaring a Student Model 
  
class Categoria_de_dimension(models.Model): 
    categoria = models.CharField( 
        max_length = 30, 
        choices = CATEGORIA_CHOICES, 
        default = '1'        ) 
    def __str__(self):
            return self.categoria

# class Categoria(models.Model):
#     name = models.CharField(max_length=30)
   

#     def __str__(self):
#         return self.name


class Figura(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class Maquina(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    figura = models.ForeignKey(Figura, on_delete = models.CASCADE)
    modelo = models.CharField(max_length=200)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    def __str__(self):
        return self.modelo


class Medidas_de_producto(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    largo_frio_predef = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    ancho_frio_predef = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    alto_frio_predef = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    flujo_de_aire_predef = models.IntegerField(blank = True, null=True)
    largo_caliente_setting_predef = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    ancho_caliente_setting_predef = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    alto_caliente_setting_predef = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    #setting = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    extrachar = models.CharField(max_length=200, blank=True,null=True)
    extrachar2 = models.CharField(max_length=200, blank=True,null=True)
    extrafloat = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    #categoria = models.ForeignKey('Categoria_de_dimension', on_delete=models.PROTECT, null=True,blank=True)
    medida_dispobible =models.BooleanField(default = True)
   
   
    def __str__(self):
        return 'Largo Frio : {0} |  Ancho Frio : {1} |  Alto Frio : {2} |  Aire : {3} |  Largo Caliente : {4} |  Ancho Caliente : {5} |  Alto Caliente : {6} |  Disponible : {7}  '   .format(
            self.largo_frio_predef,
            self.ancho_frio_predef,
            self.alto_frio_predef,
            self.flujo_de_aire_predef,
            self.largo_caliente_setting_predef,
            self.ancho_caliente_setting_predef,
            self.alto_caliente_setting_predef,
            self.medida_dispobible,
            
            )



    


class Tipo_de_espuma(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    modelo = models.CharField(max_length =200)
    modelo_id = models.CharField(max_length =200)
    medidas = models.ForeignKey(Medidas_de_producto,on_delete = models.PROTECT,blank = True, null=True)
    
    def __str__(self):
        return 'modelo: {0} | modelo_id : {1}  '   .format(self.modelo, self.modelo_id,) 

class Ajuste(models.Model):
    fechacreado = models.DateTimeField(auto_now_add=True)
    fechaactualizado = models.DateTimeField(auto_now=True)
    ajuste = models.CharField(max_length = 200)
    def __str__(self):
        return self.ajuste

#inicio,normal,cambio fin bla bla
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