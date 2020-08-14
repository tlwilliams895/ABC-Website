from django.urls import path
from .views import JoinUs

"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')"""

urlpatterns = [
    path('join_us/', JoinUs.as_view(), name='JoinUs')
]