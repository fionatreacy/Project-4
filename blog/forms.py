from .models import Comment
from django import forms

"""
    Adding comments
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)