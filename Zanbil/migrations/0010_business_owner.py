# Generated by Django 2.0.3 on 2018-05-24 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zanbil', '0009_auto_20180524_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
