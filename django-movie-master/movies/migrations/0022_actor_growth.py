# Generated by Django 4.0.6 on 2022-07-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_actor_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='growth',
            field=models.IntegerField(default=0, verbose_name='Рост'),
        ),
    ]
