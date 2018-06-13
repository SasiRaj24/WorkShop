from django import forms
from django.contrib.auth.models import User
from . import models

class MovieForm(forms.ModelForm):

    class Meta:
        model = models.movielist
        fields = ('name', 'about', 'date', 'image')


class SongForm(forms.ModelForm):

    class Meta:
        model = models.song
        fields = ('album', 'song_name', 'artist', 'song_location')