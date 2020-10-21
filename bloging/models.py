from django.db import models

# Create your models here.

class Bloging(models.Model):
	post_title = models.CharField(max_length=50)
	post_text = models.TextField()
	post_date = models.DateTimeField()
	post_image = models.ImageField(upload_to='bloging_images/')

	def get_summary(self):
		return self.post_text[:100]

	def __str__(self):
		return self.post_title