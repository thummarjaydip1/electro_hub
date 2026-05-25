from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=10,choices=(
        ('admin','admin'),
        ('user','user'),
        ('staff','staff')
    ))
    def __str__(self):
        return self.username