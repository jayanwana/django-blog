from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating an instance of the Post Model
    """
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control textinputclass'}),
            'text': forms.Textarea(attrs={'rows': '6',
                                          'class': 'editable medium-editor-textarea form-control-textarea',
                                          'width': '600px'})
        }


class CommentForm(forms.ModelForm):
    """
    Form for creating comments
    """
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control-textarea'})
        }
