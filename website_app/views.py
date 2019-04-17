from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators	 import login_required
from website_app.models import Prospect
from website_app.forms import SalesForm

# Create your views here.

class IndexView(TemplateView):
	context_object_name = 'index'
	template_name='website_app/index.html'

# class SupportCreateView(CreateView):
# 	pass

# class SupportDetailView(TemplateView):
# 	pass

class ComplianceDetailView(TemplateView):
	context_object_name = 'compliance_detail'
	template_name='website_app/compliance_detail.html'

class ProductDetailView(TemplateView):
	context_object_name = 'product_detail'
	template_name='website_app/product_detail.html'

class PricingDetailView(TemplateView):
	context_object_name = 'pricing_detail'
	template_name='website_app/pricing_detail.html'

class ServicesDetailView(TemplateView):
	context_object_name = 'ccpa_detail'
	template_name='website_app/ccpa_detail.html'

class SalesCreateView(CreateView):
	model = Prospect
	context_object_name = 'prospect_form'

	form_class = SalesForm

class SalesDetailView(TemplateView):
	context_object_name = 'prospect_detail'
	template_name='website_app/prospect_detail.html'

class VisionDetailView(TemplateView):
	context_object_name = 'vision_detail'
	template_name='website_app/vision_detail.html'

class CareersDetailView(TemplateView):
	context_object_name = 'careers_detail'
	template_name='website_app/careers_detail.html'

class FaqDetailView(TemplateView):
	context_object_name = 'faq_detail'
	template_name='website_app/faq_detail.html'


