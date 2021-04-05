# Generated by Django 3.1.7 on 2021-04-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210401_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='articles.Hashtag'),
        ),
    ]
