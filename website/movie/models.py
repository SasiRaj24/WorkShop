from django.db import models

# Create your models here.
class movielist(models.Model):
	name = models.CharField(max_length=250)
	image = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	dateofrelease = models.DateField()

	def __str__(self):
		return self.name


class song(models.Model):
	movie = models.ForeignKey(movielist, on_delete=models.CASCADE)
	songname = models.CharField(max_length=250)
	artist = models.CharField(max_length=250)

	def __str__(self):
		return self.songname