from django.urls import path
from . import views
#set your urls

urlpatterns = [
    path('',views.postview, name='home'),
    path('comment',views.comment, name='comment'),
    path('profile',views.profile, name='profile')
]
