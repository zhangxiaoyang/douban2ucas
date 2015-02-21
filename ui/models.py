from django.db import models

# Create your models here.
class DoubanUser(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=80)
    userAvatar= models.CharField(max_length=100)