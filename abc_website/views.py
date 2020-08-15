from django.views import View
from django.shortcuts import render


# Create your views here.
class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')
