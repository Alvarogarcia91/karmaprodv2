from django.db import models
# from model_utils import Choices
from django.utils import timezone
import django
import datetime
from _datetime import datetime
# from django.utils.timezone import now
# import pytz
# from django.contrib.auth.models import User
from django.urls import reverse



class Ajuste(models.Model):
    ajuste = models.CharField(max_length = 200)
    def __str__(self):
        return self.ajuste


#inicio,normal,cambio fin bla bla
class Tipo_de_unidad(models.Model):
    tipo_de_unidad = models.CharField(max_length = 100)
    def __str__(self):
        return self.tipo_de_unidad



class Cliente(models.Model):
    nombre_de_cliente = models.CharField(max_length = 200)
    tolerancia = models.IntegerField('Tolerancia del defecto')
    def __str__(self):
        return 'nombre de Cliente: {0} | puntuacion de Tolerancia: {1}  '   .format(self.nombre_de_cliente, self.tolerancia)
    


class Defecto(models.Model):
    nombre_de_defecto = models.CharField(max_length =100)
    puntuacion_de_defecto = models.IntegerField('puntuacion del defecto')
    imagen_tipo_defecto =models.CharField(max_length = 500,default="https://pbs.twimg.com/profile_images/1096162188635496449/3hAeJOKz_400x400.png ")
    def __str__(self):
        return 'nombre de defecto: {0} | puntuacion de defecto: {1}  '   .format(self.nombre_de_defecto, self.puntuacion_de_defecto,)


class Figura(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class Ubicacion(models.Model):
    ubicacion = models.CharField(max_length=200)
    def __str__(self):
        return self.ubicacion


class Maquina(models.Model):
    figura = models.ForeignKey(Figura, on_delete = models.CASCADE)
    modelo = models.CharField(max_length=200)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    ubicacion = models.ForeignKey(Ubicacion, on_delete = models.CASCADE)

    def __str__(self):
        return 'Modelo: {0} | Ubicacion: {1}  '   .format(self.modelo, self.ubicacion,)
    


class Medidas_de_producto(models.Model):
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
    modelo = models.CharField(max_length =200)
    modelo_id = models.CharField(max_length =200)
    medidas = models.ForeignKey(Medidas_de_producto,on_delete = models.CASCADE,blank = True, null=True)
    
    def __str__(self):
        return 'modelo: {0} | modelo_id : {1}  '   .format(self.modelo, self.modelo_id,) 


class Corrida(models.Model):
   
    fecha_creado = models.DateTimeField(auto_now_add=True,editable = True,blank = True, null=True)
    fecha_actualizado = models.DateTimeField(auto_now=True,editable = True,blank = True, null=True)
    fecha_a_producir = models.DateTimeField(default=datetime.now,editable = True,blank = True, null=True)
    lote = models.CharField(max_length =300)
    no_corrida = models.IntegerField()
    maquina = models.ForeignKey(Maquina,on_delete = models.CASCADE,blank = False, null=True)
    cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE,blank = False, null=True)
    auth_corrida =models.BooleanField(default = True)


    def __str__(self):
        return 'ID corrida: {0} | Lote : {1} | No.Corrida : {2} | Maquina : {3} | Cliente : {4}  | Authorizada : {5} '   .format(
        self.pk,
        self.lote,
        self.no_corrida,
        self.maquina,
        self.cliente,
        self.auth_corrida,

        ) 








#     def __str__(self):
#         return 'modelo: {0} | modelo_id : {1}  '   .format(self.user, self.created_at,) 

# class Orden_de_Corrida(models.Model):
#     modelo = models.CharField(max_length =200)
#     modelo_id = models.CharField(max_length =200)
#     medidas = models.ForeignKey(Corrida,on_delete = models.CASCADE,blank = True, null=True)
    
#     def __str__(self):
#         return 'modelo: {0} | modelo_id : {1}  '   .format(self.modelo, self.modelo_id,) 


class Espumado(models.Model):
   # al crear la corrida este numero de block se resetea
    numero_de_block = models.IntegerField()
    fecha_creado = models.DateTimeField(auto_now_add=True,editable = True,blank = True, null=True)
    fecha_actualizado = models.DateTimeField(auto_now=True,editable = True,blank = True, null=True)
    tipo_de_espuma = models.ForeignKey(Tipo_de_espuma,on_delete = models.CASCADE,blank = True, null=True)
    corrida = models.ForeignKey(Corrida,on_delete = models.CASCADE,blank = True, null=True)
    ubicacion = models.ForeignKey(Ubicacion,on_delete = models.CASCADE,blank = True, null=True)
    cliente = models.ForeignKey(Cliente,on_delete = models.CASCADE,blank = False, null=True)
    

#Parametros calientes a capturar
    largo_caliente = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    ancho_caliente= models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    alto_caliente = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)

    peso_caliente = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    flujo_de_aire = models.IntegerField(blank = True, null=True)

#formulas

    # volumen_caliente = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    @property
    def volumenf_caliente(self):
        return float(self.largo_caliente * self.ancho_caliente * abs(self.alto_caliente))

    # densidad_caliente = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    @property
    def desnidadformulaf_caliente(self):
        return float(self.peso_caliente / self.volumenf_caliente)

    tipo_de_unidad = models.ForeignKey(Tipo_de_unidad,on_delete = models.CASCADE,blank = False, null=True)
    defecto = models.ForeignKey(Defecto,on_delete = models.CASCADE,blank = True, null=True)
    ajuste = models.ForeignKey(Ajuste,on_delete = models.CASCADE,blank = True, null=True)
    nota = models.CharField(max_length = 200,blank = True, null=True)


#Parametros calientes a capturar
    largo_frio = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    ancho_frio = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    alto_frio = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    peso_frio = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    

#formulas

    # volumen_caliente = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    @property
    def volumenf_frio(self):
        return float(self.largo_frio * self.ancho_frio * abs(self.alto_frio))

    # densidad_caliente = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    @property
    def desnidadf_frio(self):
        return float(self.peso_frio / self.volumenf_frio)


    auth_corte = models.BooleanField(default = False)
#por si se dio de baja o se corto
    dispobible =models.BooleanField(default = True)




    # def __str__(self):
    #     return 'ID: {0} | puntuacion de defecto: {1}  '   .format(

    #         self.pk,
    #         # self.puntuacion_de_defecto,
            
    #         )


    # def __str__(self):
    #     return 'fecha_producido: {0} '   .format(self.fecha_producido)


    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #     return super(Cliente, self).save(*args, **kwargs)





class Meta:
    abstract = True

    def __str__(self):
        return 'fecha_producido: {0} '   .format(self.fecha_producido)


class Cilindro(Espumado):
    pass

class Block(Espumado):
    pass







