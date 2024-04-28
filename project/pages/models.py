from django.db import models
from django.utils import timezone

# Provide timezone.now() as the default value for the field
timezone.now

class Person(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return  self.user_name
    class Meta:
        verbose_name = "pizza"
        ordering = [ '-user_name']
