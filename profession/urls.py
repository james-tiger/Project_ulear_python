from django.urls import path
from . import views

urlpatterns = [
    path('', views.profession_list, name='profession_list'),
    path('about/', views.about, name='about'),
    #path('', views.statistics, name='statistics'),
    path('statistics/', views.statistics, name='statistics'),
    path('dead/<int:profession_id>/', views.deed_to_deed, name='dead')



]
