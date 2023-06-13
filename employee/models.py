from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    identification = models.FileField(upload_to='documents/')
    # Other fields for employee information

    def __str__(self):
        return self.name
