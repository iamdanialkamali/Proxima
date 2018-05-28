from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.postgres.fields import ArrayField


class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True)
    national_code = models.CharField(max_length=10, blank=True)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)


class Business(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=15)
    email = models.EmailField()
    # pics = ArrayField(models.ImageField(blank=True),blank=True,default=[])
    score = models.FloatField()
    address = models.TextField(max_length=500)
    description = models.TextField(max_length=600, default='test')
    category = models.OneToOneField(Categories, on_delete=models.DO_NOTHING)


class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    sans_count = models.IntegerField()
    work_days = ArrayField(models.IntegerField(blank=True), blank=True)
    rest_times = ArrayField(models.IntegerField(blank=True), blank=True)


class Sans(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.FloatField()
    end_time = models.FloatField()
    time_table = models.ForeignKey(to=TimeTable, on_delete=models.DO_NOTHING)


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.ForeignKey(to=Business, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    # pics = ArrayField(models.ImageField(blank=True),blank=True,default=[])
    fee = models.FloatField()
    timetable = models.ForeignKey(TimeTable, on_delete=models.DO_NOTHING)
    rating = models.FloatField()
    description = models.TextField(max_length=600, default='test')
    cancellation_fee = models.FloatField()
    cancelation_time = models.FloatField()
    capacity = models.IntegerField()
    off = models.FloatField()


class Reserves(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(to=Services, on_delete=models.DO_NOTHING, null=True)
    sans = models.ForeignKey(Sans, on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.TextField()
    date = models.CharField(max_length=150)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=600, default='test')
    rating = models.FloatField()
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING)


class pics(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=200)
    Business = models.ForeignKey(to=Business, on_delete=models.CASCADE, null=True, related_name='business')
    Service = models.ForeignKey(to=Services, on_delete=models.CASCADE, null=True, related_name='service')
    image = models.ImageField(blank=True)
