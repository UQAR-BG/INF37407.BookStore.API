from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (("A","Administrator"), ("C", "Client"))
    role = models.CharField(choices = ROLE_CHOICES, max_length=1)