from email import message
from django.db import models

# Create your models here.
class EnqData(models.Model):
    nameFirst= models.CharField(max_length=100)
    mail= models.EmailField(max_length=100)
    messageData = models.TextField(max_length=500)

    