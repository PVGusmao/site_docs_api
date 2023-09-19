from django.urls import path
from . import views

urlpatterns = [
  path('add/', views.add_patient),
  path('list/', views.get_all_patients),
]