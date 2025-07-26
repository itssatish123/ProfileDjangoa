from django.db import models
from  tinymce.models import HTMLField
class news(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    Descrition = HTMLField()


# Create your models here.
