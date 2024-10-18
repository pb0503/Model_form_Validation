from django.db import models
from django.core import validators

# Create your models here.
class Student(models.Model):
    stu_id=models.IntegerField(validators=[validators.MinValueValidator(50),validators.MaxValueValidator(100)])
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.EmailField()
    roll_no=models.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(30)])

    