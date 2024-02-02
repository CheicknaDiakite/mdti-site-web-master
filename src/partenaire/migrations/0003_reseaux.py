# Generated by Django 4.2.6 on 2023-11-07 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partenaire', '0002_alter_partenaire_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'X')], max_length=255)),
                ('url', models.URLField()),
                ('partenaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partenaire.partenaire')),
            ],
        ),
    ]
