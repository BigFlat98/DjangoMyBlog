"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import HomeView
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='home'), #views에서 확인 가능. 클래스 뷰를 사용해서 내장 함수를 사용했음.
    path('blog/',include(blog_urls)),
]
