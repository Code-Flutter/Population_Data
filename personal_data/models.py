from django.db import models
# Create your models here.

class Person(models.Model):
    sur_name = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    nin = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.given_name