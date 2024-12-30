from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DietDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fooditem = models.CharField(max_length=100)
    foodtimes = models.CharField(max_length=100)
    foodtakenday = models.CharField(max_length=100)
    takenduration = models.CharField(max_length=100)

    def __str__(self):
        return self.email

