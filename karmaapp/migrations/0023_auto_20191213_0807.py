# Generated by Django 2.2.4 on 2019-12-13 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0022_auto_20191213_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas_de_producto',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Category'),
        ),
    ]
