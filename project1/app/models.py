from django.db import models

# Create your models here.
class todo(models.Model):
    sub = models.TextField()
    date = models.DateField(auto_now_add=True,null=True)