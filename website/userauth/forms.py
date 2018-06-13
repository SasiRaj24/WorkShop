from django import forms
from django.contrib.auth.models import User
from music.models import models
class Register(forms.Form):
	first_name = forms.CharField(label='first name',max_length=20,required=False, help_text='optional')
	last_name = forms.CharField(label='last name',max_length=20,required=False, help_text='optional')
	username = forms.CharField(label='username',max_length=40,required=True)
	password1 = forms.CharField(label='password',max_length=20,required=True, widget=forms.PasswordInput )
	password2 = forms.CharField(label='Confirm password',max_length=20,required=True, widget=forms.PasswordInput )
	email = forms.CharField(label='email',max_length=40,required=True)
	bio = forms.CharField(label='User Bio',max_length=20,required=True, widget=forms.Textarea )
	date_of_birth = forms.CharField(label='date of birth',required=True,widget=forms.DateInput(attrs={'type': 'date'}))

	class Meta:
		model =User
		fields = ('username','first_name','last_name','password1','password2','email_id','bio','date_of_birth')

	def clean_username(self):
		#only one username for person
		user = self.cleaned_data.get('username').lower()
		check = User.objects.filter(username=user)
		if check.count() > 0:
			raise forms.ValidationError('The username already exists')
		return user
	def clean_password2(self):
		# check if bot passwords are equal
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Please enter same passwords both the times')
		if not(password1) and not(password2):
			raise forms.ValidationError('Please fill the password fields')
		if len(password1) < 8:
			raise forms.ValidationError('The password must be 8 chars ')
		return True

	def clean_email(self):
		# check if email is unique
		email = self.cleaned_data.get('email')
		check = User.objects.filter(email=email)
		if check.count() > 0:
			raise forms.ValidationError('The email already exists')
		return email

	def save(self):
		user = User.objects.create_user(
		username=self.cleaned_data.get('username'),
		password=self.cleaned_data.get('password1'),
		email=self.cleaned_data.get('email'),
		first_name=self.cleaned_data.get('first_name'),
		last_name=self.cleaned_data.get('last_name')
		)