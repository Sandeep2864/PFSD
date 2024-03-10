from django.urls import path
from .views import addstudent

urlpatterns = [
    path('add/', addstudent, name="add"),
]

# Create your tests here.
