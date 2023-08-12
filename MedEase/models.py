from django.db import models

# Create your models here.
class Doctor(models.Model):
    cardname = models.CharField(max_length=30)

    cardimg = models.ImageField(upload_to='pics')
    cardprofession = models.CharField(max_length=30)
    infoimg = models.ImageField(upload_to='pics/info')
    infoname = models.CharField(max_length=30)
    infoprofession = models.TextField()
    infolocation = models.CharField(max_length=30)
    infomail = models.EmailField()
    infophone = models.BigIntegerField()
    doctype = models.TextField(max_length=30)