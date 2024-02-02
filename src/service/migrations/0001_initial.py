# Generated by Django 4.2.6 on 2023-10-30 11:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
    ]