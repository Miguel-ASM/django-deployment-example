from django.db import models
from django.utils import timezone

# Create your models here.
class Rider(models.Model):
    riderName = models.CharField(max_length = 60,default = '')
    riderBirthData = models.DateField(default = timezone.now)
    riderNationality = models.CharField(max_length = 60,default = '')
    bikeBrand = models.CharField(max_length = 60,default = '')
    bikeModel = models.CharField(max_length = 60,default = '')
    def __str__(self):
        return self.riderName
