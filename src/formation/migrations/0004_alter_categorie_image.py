# Generated by Django 4.2.6 on 2023-11-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0003_remove_client_email_remove_client_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='image',
            field=models.ImageField(upload_to='1699877285.5801523'),
        ),
    ]
