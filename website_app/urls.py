from django.urls import path
from website_app import views

app_name = 'website_app'

urlpatterns = [
	path('',views.IndexView.as_view(),name='index'),
	# path('support/',views.SupportCreateView.as_view(),name='support_create'),
	# path('support/<int:pk>',views.SupportDetailView.as_view(),name='support_detail'),
	path('compliance/',views.ComplianceDetailView.as_view(),name='compliance_detail'),
	path('solutions/',views.ProductDetailView.as_view(),name='products_detail'),
	path('pricing/',views.PricingDetailView.as_view(),name='pricing_detail'),
	# https://www.okta.com/pricing/#api-base-products
	path('services/',views.ServicesDetailView.as_view(),name='services_detail'),
	path('contact-us/',views.SalesCreateView.as_view(),name='sales_create'),
	path('contact-us/<int:pk>',views.SalesDetailView.as_view(),name='sales_detail'),
	path('vision/',views.VisionDetailView.as_view(),name='vision_detail'),
	path('careers/',views.CareersDetailView.as_view(),name='careers_detail'),
	path('faq/',views.FaqDetailView.as_view(),name='faq_detail'),
]