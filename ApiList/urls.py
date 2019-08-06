"""ApiList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from main.views import CategoryListAPIView, CategoryDetail, ApiListAPIView, ApiDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/', ApiListAPIView.as_view(), name='api-list'),
     path('api/<slug:slug>/', ApiDetail.as_view(), name='api-detail'),
]
