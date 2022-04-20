# Generated by Django 4.0.4 on 2022-04-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_app', '0004_alter_city_image'),
        ('reviews_app', '0002_review_rating_culture_review_rating_food_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cities_app.city'),
        ),
    ]