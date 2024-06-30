from django.urls import path
from .views import ContactListCreate, AboutUsDetail

urlpatterns = [
    path('contact/', ContactListCreate.as_view(), name='contact_list_create'),
    path('about-us/<int:pk>/', AboutUsDetail.as_view(), name='about_us_detail'),
]
