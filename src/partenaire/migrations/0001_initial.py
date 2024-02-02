# Generated by Django 4.2.6 on 2023-10-24 09:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('site_web', models.URLField(blank=True, null=True)),
                ('numero', models.IntegerField()),
            ],
        ),
    ]