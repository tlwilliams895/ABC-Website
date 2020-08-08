from django.shortcuts import render, redirect


# Create your views here.
def join_us(request):
    message = "Aspiring Black Coders"
    return render(request, 'join_us.html')


