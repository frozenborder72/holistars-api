# Generated by Django 4.0.4 on 2022-04-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers_app', '0003_alter_follower_follower_id_alter_follower_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower_id',
            new_name='follower',
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='user_id',
            new_name='user',
        ),
    ]
