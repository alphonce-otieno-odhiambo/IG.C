from django import forms
from django.forms import fields
from .models import Comment, UserDetail, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('f_name', 'profile_pic', 'bio', 'status',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','image','caption',)