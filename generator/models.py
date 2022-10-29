from django.db import models

# Create your models here.


class Passwords(models.Model):
    password = models.CharField(max_length=50)
    created_date = models.DateField()
