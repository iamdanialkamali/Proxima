# Generated by Django 2.0.3 on 2018-04-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zanbil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
