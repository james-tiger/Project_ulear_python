"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from profession import views  # Importing all views from the profession app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    path('profession/', views.profession_list, name='profession_list'),  # Main page for professions
    path('profession/about/', views.about, name='about'),  # About page
    path('profession/statistics/', views.statistics, name='statistics'),  # Statistics page
    path('dead/<int:profession_id>/', views.deed_to_deed, name='dead')


]
