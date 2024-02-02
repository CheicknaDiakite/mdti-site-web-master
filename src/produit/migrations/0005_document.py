# Generated by Django 4.2.6 on 2023-10-25 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_rename_img_produit_image_couverture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
    ]
