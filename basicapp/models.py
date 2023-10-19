from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
