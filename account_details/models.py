from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile',null=True)
    profile_img=models.ImageField(upload_to="profile_img")
    bio=models.TextField(null=True)
    phone=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.user.userame
    
