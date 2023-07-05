from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    marks = models.DecimalField(max_digits=10,decimal_places=2)

    def _str_(self):
        return self.name
