# Generated by Django 3.1.8 on 2021-05-05 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0002_superhero_superhero_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='superhero_img',
        ),
    ]