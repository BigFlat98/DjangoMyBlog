from django.urls import path
from api import views as api_views

app_name = 'api'

urlpatterns = [
    path('post/list/',api_views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/',api_views.ApiPostDV.as_view(), name='post_Detail'),
]
