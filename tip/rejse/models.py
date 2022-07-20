from django.db import models

# Create your models here.
class rejse(models.Model):
    ferieform = models.CharField(max_length=50)
    fordel = models.TextField()
    beskrivelse = models.TextField(max_length=500)
    link = models.URLField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    