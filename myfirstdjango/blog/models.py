from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	# this is a link to another model
	author = models.ForeignKey('auth.User')
	# define text with limited no of characters
	title = models.CharField(max_length=200)
	# define long text without a limit 
	text = models.TextField()
	# date and time
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title