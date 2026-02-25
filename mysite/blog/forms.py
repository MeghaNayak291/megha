from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...', 'rows': 8}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }