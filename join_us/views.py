from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Join


def createContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
        return render(request, 'join_us/join_us.html', {'form': form})