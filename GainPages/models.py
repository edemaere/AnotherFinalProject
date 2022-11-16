from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    height_inches = models.IntegerField(default=0)
    weight_lbs = models.IntegerField(default=0)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    bench_max_lbs = models.IntegerField(default=0)
    squat_max_lbs = models.IntegerField(default=0)
    mile_time_sec = models.IntegerField(default=0)
    


    def __str__(self):
        return(self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)