from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bionic-home'),
    path('about/', views.about, name='bionic-about'),
]
