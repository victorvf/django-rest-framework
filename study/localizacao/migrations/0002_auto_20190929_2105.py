# Generated by Django 2.2.5 on 2019-09-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='referencia_dois',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
