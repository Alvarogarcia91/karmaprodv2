# Generated by Django 2.2.4 on 2019-12-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0035_auto_20191214_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas_de_producto',
            name='flujo_de_aire_predef',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
