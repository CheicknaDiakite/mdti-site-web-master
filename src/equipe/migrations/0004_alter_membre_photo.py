# Generated by Django 4.2.6 on 2023-11-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0003_membre_specialite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image: 500x500'),
        ),
    ]