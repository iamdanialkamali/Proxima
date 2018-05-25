# Generated by Django 2.0.3 on 2018-04-23 19:28

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.TextField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('pics', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), size=None)),
                ('score', models.FloatField()),
                ('address', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=600)),
                ('category_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Reserves',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('sans_no', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pic', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), size=None)),
                ('fee', models.FloatField()),
                ('rating', models.FloatField()),
                ('description', models.TextField(max_length=600)),
                ('cancellation_fee', models.FloatField()),
                ('cancelation_time', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('off', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('sans_count', models.IntegerField()),
                ('work_days', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('rest_times', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Services')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Services'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Users'),
        ),
        migrations.AddField(
            model_name='reserves',
            name='timetable_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.TimeTable'),
        ),
        migrations.AddField(
            model_name='reserves',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Zanbil.Users'),
        ),
    ]
