from django.urls import path
from . import views

app_name = 'learning_platform'

urlpatterns = [
    path('', views.learning_platform, name='learning_platform'),
]