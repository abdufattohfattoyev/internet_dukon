from django.db import models
from django.contrib.auth.models import AbstractUser
from utility.models import BaseModel


class User(AbstractUser,BaseModel):
    phone_number=models.CharField(max_length=17,null=True,blank=True,unique=True)
    age=models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.first_name


