from django import forms
from .models import Post
from django.db import models

class PostForm(forms.ModelForm):
    #post_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Post
        fields = ["post_title", "post_content", "post_image"]
