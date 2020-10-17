from django.db import models
from datetime import datetime
# Create your models here.

class Bloging(models.Model):
	post_title = models.CharField(max_length=50)
	post_text = models.TextField()
	post_date = models.DateTimeField()
	post_image = models.ImageField(upload_to='bloging_images/')