# Generated by Django 5.1.3 on 2024-12-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_image_hover_alter_service_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio'),
        ),
    ]
