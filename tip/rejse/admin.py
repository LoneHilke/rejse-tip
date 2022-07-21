from django.contrib import admin
from .models import Profile, Rejse, Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Rejse)
admin.site.register(Comment)