# Generated by Django 4.2.6 on 2023-11-06 11:26

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0002_slider_courte_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apropo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(upload_to='')),
            ],
        ),
    ]
