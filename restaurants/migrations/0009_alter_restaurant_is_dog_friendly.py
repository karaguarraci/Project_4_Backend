# Generated by Django 4.2 on 2023-04-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_remove_restaurant_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='is_dog_friendly',
            field=models.BooleanField(default=None),
        ),
    ]
