# Generated by Django 4.0.2 on 2022-07-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0028_alter_actor_career_alter_actor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='genres',
            field=models.TextField(max_length=30, verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='month',
            field=models.TextField(max_length=10, verbose_name='Месяц рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='place',
            field=models.TextField(default=0, max_length=20, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='spouse',
            field=models.TextField(max_length=30, verbose_name='Супруг'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='total_movies',
            field=models.TextField(max_length=30, verbose_name='Всего фильмов'),
        ),
    ]
