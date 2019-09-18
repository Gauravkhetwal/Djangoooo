from django.db import models

# Create your models here.

class Mobile(models.Model):
	name=models.CharField(max_length=100)
	cost=models.IntegerField(blank=True)


	def __str__(self):
		return self.name