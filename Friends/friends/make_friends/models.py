from django.db import models

class User(models.Model):
	username = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200)
	loggedin = models.IntegerField()

	def __str__(self):
		return self.name

class Friend(models.Model):
	userone = models.IntegerField()
	usertwo = models.ForeignKey(User)
