from django.urls import path
from . import views

app_name = 'job_board'

urlpatterns = [
    path('', views.get_jobs, name='get_jobs'),
]