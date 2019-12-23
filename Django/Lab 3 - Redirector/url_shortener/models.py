from django.db import models
from django.utils import timezone

class CustomURL(models.Model):
    url = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'URL code: {self.code}'
