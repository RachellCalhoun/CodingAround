from django.db import models

# Create your models here.
class Entry(models.Model):
	original_url = models.CharField(max_length = 200)
	new_url = models.CharField(max_length= 200)
	