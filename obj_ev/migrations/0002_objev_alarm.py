# Generated by Django 3.1.2 on 2022-06-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obj_ev', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objev',
            name='alarm',
            field=models.BooleanField(default=False),
        ),
    ]