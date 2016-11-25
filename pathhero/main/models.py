from __future__ import unicode_literals
from django.db import models


class Building(models.Model):
	name = models.CharField(max_length=200)
	lat = models.FloatField()
	lng = models.FloatField()

	def __unicode__(self):
		return self.name
