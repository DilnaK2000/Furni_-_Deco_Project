# Generated by Django 5.0.6 on 2024-05-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DecoApp', '0004_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Save Images'),
        ),
    ]
