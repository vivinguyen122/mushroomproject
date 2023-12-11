from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)  # make the field auto add current time and date
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # must be filled out
    username = models.CharField(max_length=255)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datetime']  # order by most recent


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FileField(upload_to='uploads', blank=True)  # blank = true makes it optional field
    datetime = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=255)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datetime']  # order by most recent
