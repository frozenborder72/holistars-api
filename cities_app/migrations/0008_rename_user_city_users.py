# Generated by Django 4.0.4 on 2022-04-22 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_app', '0007_city_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='user',
            new_name='users',
        ),
    ]
