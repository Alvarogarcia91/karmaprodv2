# Generated by Django 2.2.4 on 2019-12-13 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0018_auto_20191213_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medidas_de_producto',
            name='especial',
        ),
        migrations.RemoveField(
            model_name='medidas_de_producto',
            name='linea',
        ),
    ]
