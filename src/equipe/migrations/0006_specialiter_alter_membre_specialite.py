# Generated by Django 4.2.6 on 2023-11-09 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0005_alter_reseaux_nom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='membre',
            name='specialite',
            field=models.ForeignKey(default='Autre', on_delete=django.db.models.deletion.CASCADE, to='equipe.specialiter'),
        ),
    ]
