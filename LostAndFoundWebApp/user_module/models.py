from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class UserLostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='lost')


class UserFoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='found')


class CustomUser(AbstractUser):
    # Add any additional fields you may need
    pass
