from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.postgres.fields import ArrayField


class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20,blank=True)
    national_code = models.CharField(max_length=10,blank=True)
    history =ArrayField(models.PositiveIntegerField(blank=True,default=0),blank=True,default=[0])
    

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

class Business(models.Model):
    owner=models.ForeignKey(Users ,on_delete=models.DO_NOTHING,null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=15)
    email = models.EmailField()
    pics = ArrayField(models.ImageField(blank=True),blank=True,default=[])
    score = models.FloatField()
    address = models.TextField(max_length=500)
    description = models.TextField(max_length=600,default='test')
    category_id = models.OneToOneField(Categories ,on_delete=models.DO_NOTHING)


class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(auto_now=True)
    sans_count = models.IntegerField()
    work_days  = ArrayField(models.IntegerField(blank=True),blank=True)
    rest_times = ArrayField(models.IntegerField(blank=True),blank=True)

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    business=models.ForeignKey(to=Business,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    pics = ArrayField(models.ImageField(blank=True),blank=True,default=[])
    fee = models.FloatField()
    timetable=models.ForeignKey(TimeTable,on_delete=models.DO_NOTHING)
    rating = models.FloatField()
    description = models.TextField(max_length= 600,default='test')
    cancellation_fee = models.FloatField()
    cancelation_time = models.FloatField()
    capacity = models.IntegerField()
    off = models.FloatField()

class Reserves(models.Model):
    id = models.AutoField(primary_key=True)
    timetable_id = models.ForeignKey(TimeTable,on_delete=models.DO_NOTHING,)
    user_id = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    description = models.TextField()
    sans_no = models.PositiveIntegerField()
    date= models.DateTimeField(auto_now=True)
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    description=models.CharField(max_length=600,default='test')
    rating = models.FloatField()
    user_id= models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    service_id= models.ForeignKey(Services,on_delete=models.DO_NOTHING)
