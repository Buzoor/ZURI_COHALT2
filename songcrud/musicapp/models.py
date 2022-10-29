from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=250)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
