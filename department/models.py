from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    # Other fields for department information

    def __str__(self):
        return self.name