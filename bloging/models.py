from django.db import models
from datetime import datetime
# Create your models here.

class Bloging(models.Model):
	post_image = models.ImageField(upload_to='bloging_images/')
	post_text = models.CharField(max_length=1000)
	post_title = models.CharField(max_length=50)
	post_date = models.DateTimeField()