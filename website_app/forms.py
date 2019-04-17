from django import forms
from django.forms import ModelForm
from website_app.models import Prospect




class SalesForm(forms.ModelForm):

	class Meta:
		model = Prospect
		fields = ['first_name','last_name','company','email','phone','message']

