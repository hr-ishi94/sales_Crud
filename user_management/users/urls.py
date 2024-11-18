from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('register/',views.RegisterView.as_view(),name='user-register'),
    
]
