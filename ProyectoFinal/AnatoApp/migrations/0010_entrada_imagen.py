# Generated by Django 4.2 on 2023-05-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnatoApp', '0009_delete_alumno_delete_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
