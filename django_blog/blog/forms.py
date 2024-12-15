from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# blog/forms.py

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
from django import forms
from .models import Post, Tag
from taggit.forms import TagWidget
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
from django import forms
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    # Use TagWidget to render the tag input field
    tags = forms.CharField(widget=TagWidget(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
