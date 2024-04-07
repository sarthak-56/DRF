from django.db import models

# company model
class Company(models.Model):
    IT = 'IT'
    NON_IT = 'NON IT'
    CALLTELLER = 'Callteller'

    TYPE_CHOICES = [
        (IT, 'IT'),
        (NON_IT, 'NON IT'),
        (CALLTELLER, 'Callteller'),
        
    ]

    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    your_field = models.CharField(max_length=20, choices=TYPE_CHOICES)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# Employee model
class Employee(models.Model):

    name = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    about=models.TextField(max_length=50)
    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Leader', 'Project Leader'),
    ]

    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)    