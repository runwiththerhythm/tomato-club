from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    favourite_tomato = models.CharField(max_length=100, blank=True)
    avatar = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.user.username
