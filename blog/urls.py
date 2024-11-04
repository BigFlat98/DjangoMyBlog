from django.contrib import admin
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('post/<int:pk>/',views.PostDV.as_view(),name='post_detail'),
]