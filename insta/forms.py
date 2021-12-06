from django import forms
from .models import Comment, UserDetail

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment')


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ("profile_pic","f_name","bio", "status")