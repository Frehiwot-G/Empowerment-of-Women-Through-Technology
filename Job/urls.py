from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('post_job/',post_job,name='post_job'),
]