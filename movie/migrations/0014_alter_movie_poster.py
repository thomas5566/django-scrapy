# Generated by Django 3.2 on 2020-09-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='movie/images/', verbose_name='Poster'),
        ),
    ]