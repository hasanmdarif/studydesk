from blog import views
from django.urls import path, include

urlpatterns = [
    path('contact/', views.contactUs, name='contact')
]