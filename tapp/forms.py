from django import forms 
from .models import BlogComment , Subscribe , Client , Blog , ArticaleContact , Contact , Review
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = [
            'name',
            'post_comment'
        ]

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = [
            'email'
        ]
    
class feedbackForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'message',
            'image'
        ]
    
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'categorys',
            'title',
            'details',
            'image'
        ]

class ArticaleContactForm(forms.ModelForm):
    class Meta:
        model = ArticaleContact
        fields = [
            'name',
            'phone',
            'message'
        ]

    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'name',
            'mark',
            'comment'
        ]
