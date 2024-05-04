from django.db import models

class Book(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    launch = models.IntegerField(null=False, blank=False)
    edition = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=200, null=False, blank=False)
    gender = models.CharField(max_length=200, null=False, blank=False)
    publisher = models.CharField(max_length=200, null=False, blank=False)
    year_edition = models.IntegerField(null=False, blank=False)
    edition_number = models.IntegerField(null=False, blank=False)