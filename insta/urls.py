from django.urls import path
from . import views
#set your urls

urlpatterns = [
    path('', views.register_view, name = 'register'),
    path('login',views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('home',views.postview, name='home'),
    path('comment',views.comment, name='comment'),
    path('profile',views.profile, name='profile'),
    path('post',views.post, name='post'),
    path('profile_page',views.profile_page, name='profile_page'),
    path('followercount',views.followercount, name='followercount'),
]
