from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Userdetail(models.Model):
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    userpoints=models.IntegerField(default="10")
    profile_img=models.ImageField(upload_to='',default="images\default.png")
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    


    def __str__(self):
        return self.gender
    