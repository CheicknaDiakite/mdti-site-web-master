# Generated by Django 4.2.6 on 2023-10-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membre',
            old_name='img',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='membre',
            name='numero',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
