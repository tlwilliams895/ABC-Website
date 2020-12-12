from django.urls import path
from .views import createContact

app_name = 'join_us'

urlpatterns = [
    path('', createContact, name='contact'),
]