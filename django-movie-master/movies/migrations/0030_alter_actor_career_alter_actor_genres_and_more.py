# Generated by Django 4.0.2 on 2022-07-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0029_alter_actor_genres_alter_actor_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='career',
            field=models.CharField(max_length=40, verbose_name='Карьера'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='genres',
            field=models.CharField(max_length=30, verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='month',
            field=models.CharField(max_length=10, verbose_name='Месяц рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='place',
            field=models.CharField(max_length=20, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='spouse',
            field=models.CharField(max_length=30, verbose_name='Супруг'),
        ),
    ]
