from django.db import models
from django.contrib.auth.models import User
'''
class addquestion(models.Model):
    question=models.TextField()
    answer=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    


    def __str__(self):
        return self.user

'''
class Userdata(models.Model):
    question=models.TextField()
    ans=models.TextField()
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    
    
    


    def __str__(self):
        return self.user.username