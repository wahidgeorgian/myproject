from dataclasses import field
from pyexpat import model
from django import forms
from .models import Post, User, Comment
from django.contrib.auth.forms import UserCreationForm  

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['author','title','text','category','tag','thumbnail','feature',]

# Form for registration

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email","mobile_number","city","state","country","image",)


class LoginForm(forms.Form):
    
    username =forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'username',
            'email',
            
        )
       