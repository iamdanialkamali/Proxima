# Generated by Django 2.0.3 on 2018-05-28 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zanbil', '0020_auto_20180528_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='business',
        ),
        migrations.AddField(
            model_name='reserves',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Services'),
        ),
    ]