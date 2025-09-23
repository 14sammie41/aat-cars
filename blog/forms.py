from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for adding comments to a blog post."""
    class Meta:
        model = Comment
        fields = ['body']