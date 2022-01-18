from django.db import models
from django.contrib.contenttypes.models import ContentType

from teacher.models import Teacher

# Create your models here.

# SchoolProfile model 
class SchoolProfile(models.Model):
    name = models.CharField(max_length=255)
    principal = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    npsn = models.CharField(max_length=255)
    accreditation = models.CharField(max_length=1)
    image = models.ImageField(blank=False, null=False, default="/media/elon_musk.jpg")
    image2 = models.ImageField(blank=False, null=False, default="/media/elon_musk.jpg")
    image3 = models.ImageField(blank=False, null=False, default="/media/elon_musk.jpg")
    address = models.TextField()
    general_info = models.TextField()
    email = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=255)

# class ImageProperty(models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     image = models.ImageField(blank=False, null=False)