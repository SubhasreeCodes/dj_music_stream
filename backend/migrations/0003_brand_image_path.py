# Generated by Django 5.1.6 on 2025-02-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image_path',
            field=models.ImageField(default='no_image_available.png', upload_to='brand'),
        ),
    ]
