from django.urls import path
from .views import createContact


urlpatterns = [
    path('join_us/', createContact, name='contact')
]