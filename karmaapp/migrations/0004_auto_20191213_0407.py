# Generated by Django 2.2.4 on 2019-12-13 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0003_defecto_tipo_de_unidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defecto',
            old_name='nombredefecto',
            new_name='nombre_de_defecto',
        ),
        migrations.RenameField(
            model_name='tipo_de_unidad',
            old_name='tipounidad',
            new_name='tipo_de_unidad',
        ),
    ]
