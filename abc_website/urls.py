"""abc_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import index, mission #Imports the index view which we created in views.py file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),#Path to the index.html template. Empty quotes are equivalent to '/' or localhost8000
    path('mission/', mission, name='mission'),
    path('', include('job_board.urls')),
]
