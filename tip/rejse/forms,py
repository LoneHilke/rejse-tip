from django.db import forms
from .models import Profile, Rejse, Comment 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Rejse
        fields = ('title', 'ferieform', 'slug', 'content', 'fordel', 'beskrivelse', 'link', 'img')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'ferieform': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
            'fordel': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'beskrivelse': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
        }
