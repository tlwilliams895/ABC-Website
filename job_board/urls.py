from django.urls import path
from . import views

urlpatterns = [
    path('job_board/', views.get_jobs, name='get_jobs')
]
