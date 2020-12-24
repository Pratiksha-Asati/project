from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    email_id=models.EmailField(max_length=25)
    password=models.CharField(max_length=25,null=True)

# Create your models here.
