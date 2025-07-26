from django.db import models

class education(models.Model):
    Edu_date = models.CharField(max_length=50)
    Edu_title = models.CharField(max_length=100)
    Edu_Desc = models.TextField()


# Create your models here.
