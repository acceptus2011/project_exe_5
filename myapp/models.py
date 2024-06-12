from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class SpaUser(AbstractUser):
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=10000)