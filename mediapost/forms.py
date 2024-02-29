from django import forms
from .models import SocialMediaPost

class SocialMediaPostForm(forms.ModelForm):
    class Meta:
        model = SocialMediaPost
        fields = ['title', 'description', 'scheduled_time']
