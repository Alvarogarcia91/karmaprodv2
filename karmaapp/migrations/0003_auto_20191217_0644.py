# Generated by Django 2.2.4 on 2019-12-17 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0002_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]