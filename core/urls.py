from django.urls import path
from core.views import create_lead

urlpatterns = [
    path('api/create_lead/', create_lead, name='create_lead'),
]