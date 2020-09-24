
from django.urls import path
from uapi import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('download', views.Youtube_downloader.as_view()),
]