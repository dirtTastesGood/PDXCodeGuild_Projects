from django.db import models
from PIL import Image

from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile_images/default1.png', upload_to='profile_images')

