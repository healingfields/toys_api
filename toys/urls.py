from django.urls import path 
from . import views

urlpatterns = [
  path('toys', views.toy_list),
  path('toys/<pk>', views.toy_details),
]