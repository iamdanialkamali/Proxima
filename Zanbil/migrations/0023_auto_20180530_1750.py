# Generated by Django 2.0.2 on 2018-05-30 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zanbil', '0022_sans_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Categories'),
        ),
    ]