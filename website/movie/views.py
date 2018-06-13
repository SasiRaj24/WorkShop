from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
# Create your views here.
def movie(request):
	return HttpResponse(" Movies will be displayed here")
class list(generic.ListView):
	model = models.movielist
	context_object_name = 'movie_list'
	template_name='movie/sample.html'
def detail(request,pk):
	movie=models.movielist.objects.get(pk=pk)
	return render(request, 'movie/detailv.html',{'movie':movie})