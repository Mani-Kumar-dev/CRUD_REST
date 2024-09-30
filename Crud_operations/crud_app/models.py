from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=256)
    def __str__(self):
        return self.title
    
class Designation(models.Model):
    title = models.CharField(max_length=256)
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=256)
    email = models.EmailField()
    department =models.ForeignKey(Department,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    Location = models.CharField(max_length=256)
    def __str__(self):
        return self.name