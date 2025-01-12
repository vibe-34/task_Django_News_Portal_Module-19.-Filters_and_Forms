from django import forms
from django_filters import CharFilter

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', ]
