from django.db import models

class todo(models.Model):
    task=models.CharField(max_length=50)

class product(models.Model):
    name=modles.CharField(max_length=50)
    desc=modles.CharField(max_length=100)
    price=models.IntegerField()
    url = CharField(max_length=200)