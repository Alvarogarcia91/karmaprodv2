# Generated by Django 2.2.4 on 2019-12-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0027_auto_20191213_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas_de_producto',
            name='extrachar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medidas_de_producto',
            name='extrachar2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
