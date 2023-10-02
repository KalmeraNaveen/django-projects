from django.db import models

# Create your models here.
class Hellomodel(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField()
