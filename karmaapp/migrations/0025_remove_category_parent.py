# Generated by Django 2.2.4 on 2019-12-13 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0024_auto_20191213_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]