# Generated by Django 4.2.6 on 2023-11-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0003_apropo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image: 1920x1080'),
        ),
    ]
