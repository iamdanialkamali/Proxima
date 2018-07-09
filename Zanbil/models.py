from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True)
    national_code = models.CharField(max_length=10, blank=True)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Business(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=15)
    email = models.EmailField()
    # pics = ArrayField(models.ImageField(blank=True),blank=True,default=[])
    score = models.FloatField(default=0)
    address = models.TextField(max_length=500)
    description = models.TextField(max_length=600, default='test')
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    image =models.ImageField(default='2.jpg')

    def __str__(self):
        return self.name

    def calculateScore(self, sc):
        return (self.score + sc) / 2


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
    weekday = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.start_time) + 'to' + str(self.end_time)


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.ForeignKey(to=Business, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    # pics = ArrayField(models.ImageField(blank=True),blank=True,default=[])
    fee = models.FloatField()
    timetable = models.ForeignKey(TimeTable, on_delete=models.DO_NOTHING)
    rating = models.FloatField(default=0)
    description = models.TextField(max_length=600, default='test')
    cancellation_fee = models.FloatField(default=0)
    cancelation_time = models.FloatField(default=0)
    capacity = models.IntegerField()
    off = models.FloatField(default=0)
    firstSans = models.FloatField(default=8)
    lastSans = models.FloatField(default=20)
    restTimeStart = models.FloatField(default=12)
    restTimeEnd = models.FloatField(default=12)


    def __str__(self):
        return self.name


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
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.description


class pics(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=200)
    Business = models.ForeignKey(to=Business, on_delete=models.CASCADE, null=True, related_name='business')
    Service = models.ForeignKey(to=Services, on_delete=models.CASCADE, null=True, related_name='service')
    image = models.ImageField(blank=True)

class Test(models.Model):
    name = models.CharField(max_length =100)
    image = models.ImageField()
