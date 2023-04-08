from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('module/',modulePage,name='module'),
    path('mentors/',mentorsPage,name='mentors'),
    path('record_book/',record_book,name='record_book'),
    path('record_skill/',record_skills,name='record_skills'),
    path('register_mentor/',register_mentor,name='register_mentor')
]