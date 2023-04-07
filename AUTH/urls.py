from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user,register_care_givers,home

urlpatterns = [
    path('home/',home,name='home'),
    path('register_user/',register_user,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='AUTH/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='AUTH/logout.html'), name='logout'),
    path('register_caregivers/',register_care_givers,name='register'),
]