from django.db import models
from django.urls import reverse

# Create your models here.

class Prospect(models.Model):

	first_name = models.CharField(max_length=256,blank=False)
	last_name = models.CharField(max_length=256,blank=False)
	company = models.CharField(max_length=256,blank=False)
	email = models.EmailField(max_length=256,blank=False)
	phone = models.CharField(max_length=15,blank=True)
	message = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name + " " + self.last_name + " (" + self.email + ")"

	def get_absolute_url(self):
		return reverse('website_app:sales_detail',kwargs={'pk':self.pk})
