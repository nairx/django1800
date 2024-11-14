from django.db import models

class todo(models.Model):
    task=models.CharField(max_length=50)

class product(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    price=models.IntegerField()
    url =models.CharField(max_length=200)