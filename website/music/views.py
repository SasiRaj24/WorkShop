from django.views import generic
from . import models
from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def music(request):
	if request.user.is_authenticated:
		movies = models.movielist.objects.all()
		return render(request,'music/home.html',{'movie_list': movies})
	else:
		return HttpResponse("You need to access to hear the SONGS")

def listsong(request,pk):
	if request.user.is_authenticated:
		movie = models.movielist.objects.get(pk=pk)
		return render(request, 'music/list.html',{'album':movie})
	else:
		return HttpResponse("You Needd Access")
def add_movie(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.MovieForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("movie saved")
        else:
            form = forms.MovieForm()
        return render(request, 'music/setting.html', {'form': form})
    else:
        return HttpResponse("you need to login to access song")

def add_song(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.SongForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("song saved")
        else:
            form = forms.SongForm()
        return render(request, 'music/songsave.html', {'form': form})
    else:
        return HttpResponse("you need to login to access song")