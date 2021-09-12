from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='Name')
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    location = models.CharField(max_length=40)
    time = models.DateTimeField()
    likes = models.ManyToManyField(
        to=User,  related_name='likes', null=True, blank=True)
