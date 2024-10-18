from django.db import models
from django.core import validators

# Create your models here.
class Resident(models.Model):
    full_name=models.CharField(max_length=50)
    society_name=models.CharField(max_length=50)
    wing_name=models.CharField(max_length=50)
    flat_no=models.IntegerField(validators=[validators.MinValueValidator(101),validators.MaxValueValidator(1006)])

    