from django.urls import path
from api import views as api_views

app_name = 'api'

urlpatterns = [
    path('post/list/',api_views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/',api_views.ApiPostDV.as_view(), name='post_Detail'),
    path('catetag/',api_views.ApiCateTagView.as_view(), name='catetag_list'),
    path('like/<int:pk>/',api_views.ApiPostLikeDV.as_view(), name='post_like'),
    path('comment/create/',api_views.ApiCommentCV.as_view(), name='comment_create'),
]
