# Generated by Django 3.1.7 on 2021-04-01 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210401_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='following',
            new_name='followings',
        ),
    ]
