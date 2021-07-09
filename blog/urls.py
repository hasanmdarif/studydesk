from blog import views
from django.urls import path, include

urlpatterns = [
    path('contact/', views.contactUs, name='contact'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about', views.AboutUs.as_view(), name='about'),
    path('search', views.search, name='search'),
]

