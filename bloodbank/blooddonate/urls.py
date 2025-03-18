from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_user, name='login'),  # Login page
    path('register-blood-bank/', views.register_blood_bank, name='register_blood_bank'),  # Register blood bank
    path('register-donor/', views.register_donor, name='register_donor'),  # Register donor
]
