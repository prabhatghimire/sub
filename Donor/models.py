from django.db import models
from django.contrib.auth.admin import User




# Create your models here.
#news and event table
class Event(models.Model):
	title = models.CharField(max_length=140)
	anouncedate = models.DateTimeField()
	detail = models.TextField(max_length=1400000000)
	photo = models.FileField()
	organizer = models.CharField(max_length=140)
	location = models.CharField(max_length=140)
	posteddate = models.DateTimeField(auto_now=True)
	# slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

# list of bloodbank table
class Bloodbank(models.Model):
	name = models.CharField(max_length=140)
	phone = models.CharField(max_length=140)
	loaction = models.CharField(max_length=140)

	def __str__(self):
		return self.name

#Feedback table
class Feedback(models.Model):
	name = models.CharField(max_length=140)
	email = models.EmailField(max_length=140)
	subject = models.CharField(max_length=140)
	comment = models.CharField(max_length=140)

	def __str__(self):
		return self.name
