from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    

    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return self.caption

class Comment(models.Model):
    comtt = models.ForeignKey('Post', null=True, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)
    followers = models.ManyToManyField(Post, blank=True, related_name='followers')


    def __str__(self):
        return self.comment

    #def save(self):
        #self.save()
class UserDetail(models.Model):
    f_name = models.CharField(max_length=200)
    profile_pic = CloudinaryField('image')
    bio = models.CharField(max_length=200)
    status = models.CharField(max_length=300)
    

    def __str__(self):
        return self.f_name

class FollowersCount(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user