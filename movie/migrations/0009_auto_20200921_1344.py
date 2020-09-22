# Generated by Django 3.2 on 2020-09-21 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieyear', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.ForeignKey(default=2020, on_delete=django.db.models.deletion.CASCADE, to='movie.movieyears'),
            preserve_default=False,
        ),
    ]
