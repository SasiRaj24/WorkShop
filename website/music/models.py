from django.db import models
# Create your models here.
from django.utils import timezone

class movielist(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    image = models.FileField(upload_to='pictures/')
    date = models.DateField()
    upload_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

class song(models.Model):
    album = models.ForeignKey( movielist, on_delete=models.CASCADE )
    song_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    song_location = models.FileField(upload_to="")
    
    def __str__(self):
        return self.song_name