from rest_framework import generics
from apps.core.models import Contact, AboutUs
from .serializers import ContactSerializer, AboutUsSerializer

class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutUsDetail(generics.RetrieveUpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
