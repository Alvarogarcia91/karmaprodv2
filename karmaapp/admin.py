from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin


@admin.register(
    Cilindro,
    Block,
    Tipo_de_espuma,
    Tipo_de_unidad,
    Defecto,
    Ajuste,
    Cliente,
    Medidas_de_producto, 
    # Categoria,
    # Categoria_de_dimension,
    Maquina,
    Figura,
    Ubicacion,
    Espumado,
    Corrida,
    


    
    )
class ViewAdmin(ImportExportModelAdmin):
    pass


