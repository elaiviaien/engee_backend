# Generated by Django 3.1.2 on 2022-06-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20220609_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]