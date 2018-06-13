from django.db import models
from . import forms
from django.contrib.auth.models import User
# Create your models here.

class Otherdetail(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=250)
	dob = models.DateField()