from django.db import models

# Create your models here.
class Encyclopedia(models.Model):
    title = models.CharField(primary_key=True, max_length=64)
    content = models.TextField()
