from django.db import models



class Project(models.Model):
    
    title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    text = models.CharField(max_length=400, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    icons = models.ImageField(upload_to='icons', null=True, blank=True)

class Skill(models.Model):

    title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    icons = models.ImageField(upload_to='icons', null=True, blank=True)

    