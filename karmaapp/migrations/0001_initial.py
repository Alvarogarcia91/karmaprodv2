# Generated by Django 2.2.4 on 2019-12-16 12:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajuste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ajuste', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_cliente', models.CharField(max_length=200)),
                ('tolerancia', models.IntegerField(verbose_name='Tolerancia del defecto')),
            ],
        ),
        migrations.CreateModel(
            name='Corrida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_actualizado', models.DateTimeField(auto_now=True, null=True)),
                ('fecha_a_producir', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('lote', models.CharField(max_length=300)),
                ('no_corrida', models.IntegerField()),
                ('auth_corrida', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Defecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_defecto', models.CharField(max_length=100)),
                ('puntuacion_de_defecto', models.IntegerField(verbose_name='puntuacion del defecto')),
                ('imagen_tipo_defecto', models.CharField(default='https://pbs.twimg.com/profile_images/1096162188635496449/3hAeJOKz_400x400.png ', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Espumado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_block', models.IntegerField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_actualizado', models.DateTimeField(auto_now=True, null=True)),
                ('largo_caliente', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('ancho_caliente', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('alto_caliente', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('peso_caliente', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('flujo_de_aire', models.IntegerField(blank=True, null=True)),
                ('nota', models.CharField(blank=True, max_length=200, null=True)),
                ('largo_frio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ancho_frio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alto_frio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('peso_frio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('auth_corte', models.BooleanField(default=False)),
                ('dispobible', models.BooleanField(default=True)),
                ('ajuste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Ajuste')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Cliente')),
                ('corrida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Corrida')),
                ('defecto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Defecto')),
            ],
        ),
        migrations.CreateModel(
            name='Figura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medidas_de_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo_frio_predef', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('ancho_frio_predef', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('alto_frio_predef', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('flujo_de_aire_predef', models.IntegerField(blank=True, null=True)),
                ('largo_caliente_setting_predef', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('ancho_caliente_setting_predef', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('alto_caliente_setting_predef', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('extrachar', models.CharField(blank=True, max_length=200, null=True)),
                ('extrachar2', models.CharField(blank=True, max_length=200, null=True)),
                ('extrafloat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('medida_dispobible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_de_unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_unidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('espumado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karmaapp.Espumado')),
            ],
            bases=('karmaapp.espumado',),
        ),
        migrations.CreateModel(
            name='Cilindro',
            fields=[
                ('espumado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karmaapp.Espumado')),
            ],
            bases=('karmaapp.espumado',),
        ),
        migrations.CreateModel(
            name='Tipo_de_espuma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('modelo_id', models.CharField(max_length=200)),
                ('medidas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Medidas_de_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('figura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Figura')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Ubicacion')),
            ],
        ),
        migrations.AddField(
            model_name='espumado',
            name='tipo_de_espuma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Tipo_de_espuma'),
        ),
        migrations.AddField(
            model_name='espumado',
            name='tipo_de_unidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Tipo_de_unidad'),
        ),
        migrations.AddField(
            model_name='espumado',
            name='ubicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Ubicacion'),
        ),
        migrations.AddField(
            model_name='corrida',
            name='maquina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='karmaapp.Maquina'),
        ),
    ]
