# Generated by Django 2.2 on 2019-05-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biljnevrsteapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uporabnidio',
            name='biljna_vrsta',
        ),
        migrations.AddField(
            model_name='biljnavrsta',
            name='uporabni_dio',
            field=models.ManyToManyField(to='biljnevrsteapp.UporabniDio'),
        ),
    ]
