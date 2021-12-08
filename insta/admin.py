from django.contrib import admin
from .models import Post, Comment, UserDetail, FollowersCount

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserDetail)
admin.site.register(FollowersCount)
