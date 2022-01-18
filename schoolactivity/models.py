from django.db import models

# Create your models here.
class SchoolActivity(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=False, null=False, default="/media/elon_musk.jpg")
    description = models.TextField()