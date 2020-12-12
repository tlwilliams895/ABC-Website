from django.urls import path
from . import views

app_name = 'learning_platform'

urlpatterns = [
    path('', views, name='contact'),
]