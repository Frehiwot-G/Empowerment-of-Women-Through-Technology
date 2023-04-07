from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user,register_care_givers,home

# urlpatterns = [
#      path('register_client/',register_client.as_view(template_name='client/register.html'), name='register'),
#      path('register_caregivers/',register_care_givers.as_view(template_name='caregiver/register.html'), name='register'),
#      path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#      path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
# ]
urlpatterns = [
    path('home/',home,name='home'),
    path('register_user/',register_user,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register_caregivers/',register_care_givers,name='register'),
]