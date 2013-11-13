from django.db import models

# Create your models here.

class Redis_Servers (models.Model):
	host = models.TextField(default="127.0.0.1", null=False, blank=False)
	port = models.IntegerField(default=6379, null=False, blank=False)
	db = models.SmallIntegerField(default=0, null=False, blank=False)

class Redis_stat (models.Model):
	server = models.ForeignKey(to=Redis_Servers)
	timestamp = models.DateTimeField(auto_now=True, null=False, blank=False)
	keys_count = models.IntegerField(default=0, blank=True, null=False)