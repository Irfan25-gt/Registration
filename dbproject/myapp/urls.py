from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about_form),
    path('registration/', views.registration_form),
    path('add-std/', views.save, name="add"),
    path('display/', views.std_list),
]