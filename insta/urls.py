from django.urls import path
from . import views
#set your urls

urlpatterns = [
    
    
    path('',views.postview, name='home'),
    path('comment',views.comment, name='comment'),
    path('profile',views.profile, name='profile'),
    path('post',views.post, name='post'),
    path('profile_page',views.profile_page, name='profile_page'),
    path('followercount',views.followercount, name='followercount'),
]
