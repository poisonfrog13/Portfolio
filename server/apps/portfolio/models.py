from django.db import models



class Projects(models.Model):
    
    title = models.CharField(max_length=100, null=False)
    subtitle = models.CharField(max_length=200, null=False)
    text = models.CharField(max_length=400, null=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    icons = models.ImageField(upload_to='icons', null=True, blank=True)

class Skills(models.Model):

    title = models.CharField(max_length=100, null=False)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    icons = models.ImageField(upload_to='icons', null=True, blank=True)

    