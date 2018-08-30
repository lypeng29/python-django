from django.db import models

class Articles(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.title