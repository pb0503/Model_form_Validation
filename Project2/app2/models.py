from django.db import models
from django.core import validators


# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(100)])
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(150)])

    