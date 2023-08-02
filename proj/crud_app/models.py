from django.db import models

class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    adds = models.CharField(max_length=50)
    