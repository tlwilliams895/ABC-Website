from django.urls import path
from . import views

urlpatterns = [
    path('join_us/', views.join_us, name='join_us')
]