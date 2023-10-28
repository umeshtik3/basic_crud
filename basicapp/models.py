from django.db import models

# Create your models here.

from enum import Enum

class Department(Enum):
    HR = 'HR'
    IT = 'IT'
    SALES = 'Sales'
    MARKETING = 'Marketing'
    FINANCE = 'Finance'
    OPERATIONS = 'Operations'
    CUSTOMER_SERVICE = 'Customer Service'
    ADMINISTRATION = 'Administration'
    RESEARCH_AND_DEVELOPMENT = 'R&D'
    PROCUREMENT = 'Procurement'


class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100,choices=[(department.name,department.value) for department in Department])
