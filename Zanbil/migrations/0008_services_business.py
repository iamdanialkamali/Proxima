# Generated by Django 2.0.3 on 2018-05-24 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zanbil', '0007_auto_20180524_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='business',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Business'),
            preserve_default=False,
        ),
    ]
