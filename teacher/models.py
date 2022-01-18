from django.db import models
from major.models import Major

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    born_date = models.DateField()
    nip = models.CharField(max_length=255)
    image = models.ImageField(blank=False, null=False, default="/media/elon_musk.jpg")
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    born_date = models.DateField()
    position = models.CharField(max_length=255)
    active_date = models.DateField()
    deactivated_date = models.DateField()