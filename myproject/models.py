from django.db import models

class Subscribers(models.Model):
	email = models.Charfield(max_lenght=1000, blank=False, null=False, help_text='Email address')
	full_name = models.charfield(max_lenght=1000, blank=False, null=false, help_text='First and last name')
	
	def __str__(self):
		return self.full_name
		
	class Meta:
		verbose_name = "Subscriber"
		verbose_name_plural "Subscribers"	
