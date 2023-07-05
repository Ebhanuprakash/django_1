from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Task(models.Model):
    Email_id = models.EmailField(User, unique=True)
    Account_id = models.UUIDField(User,primary_key=True, default=uuid.uuid4, editable=False)
    Account_name = models.CharField(User,max_length=255)
    Website = models.URLField(User,blank=True)

    def __str__(self):
        return self.Website

    
    
