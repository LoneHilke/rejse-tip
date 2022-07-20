import re
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
 
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)



class Rejse(models.Model):
    title=models.CharField(max_length=255)
    ferieform = models.CharField(max_length=50, blank=True, null=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    fordel = models.TextField()
    beskrivelse = models.TextField(max_length=500)
    link = models.URLField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.author) + " Titel" + self.title

    def get_absolute_url(self):
        return reverse('ferie')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(Rejse, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)
 
    def __str__(self):
        return self.user.username +  " Comment: " + self.content
