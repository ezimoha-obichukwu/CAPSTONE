# Generated by Django 4.2.2 on 2023-06-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0005_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
