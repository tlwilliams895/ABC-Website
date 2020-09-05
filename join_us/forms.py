from django import forms
from .models import Join


class ContactForm(forms.ModelForm):
    class Meta(object):
        model = Join
        fields = ('name', 'emailAddress', 'phoneNumber')