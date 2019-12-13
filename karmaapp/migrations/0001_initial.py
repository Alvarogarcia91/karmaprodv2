# Generated by Django 2.2.4 on 2019-12-13 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Espumado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_producido', models.CharField(max_length=200)),
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
    ]
