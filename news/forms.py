from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, FileInput, MultipleChoiceField, ChoiceField
from .models import Post

class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'placeholder': 'title'}),
            'body': TextInput(attrs={'placeholder': 'body'}),
            'date_published': TextInput(attrs={'placeholder': 'Date and Time'}),
            'post_image': FileInput(attrs={'placeholder': 'Drop your image here'})


        }

