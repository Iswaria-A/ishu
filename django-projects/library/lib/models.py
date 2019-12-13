from django.db import models
class books(models.Model):
	name=models.CharField(max_length=100)
	author_name=models.CharField(max_length=100)
	year=models.IntegerField()
	price=models.IntegerField()
	def __str__(self):
		return slf.name
