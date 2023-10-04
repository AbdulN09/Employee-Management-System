from django.db import models

class Employee(models.Model):
    employeeId = models.CharField(primary_key=True, max_length=100)
    fullName = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    nationality = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    projects = models.CharField(max_length=255)
    promoted = models.BooleanField(default=False)

    def __str__(self):
        return self.fullName
