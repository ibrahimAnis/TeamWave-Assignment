from django.db.models import JSONField
from django.db import models

class Cache(models.Model):
	query = models.CharField(max_length=1000)
	data = JSONField(null=True)
	def __str__(self):
		return self.query

	
