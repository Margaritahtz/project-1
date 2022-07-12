from django.urls import path
from . import views


urlpatterns = [
   #('', views.loginpage, name='login'),
   path('dashboard/', views.dashboard, name='dashboard')
]

