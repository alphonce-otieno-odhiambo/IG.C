from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(blank = True, null = True , upload_to = "media/images/")
    caption = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

class Comment(models.Model):
    comment = models.TextField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        self.comment

    def save(self):
        self.save()
