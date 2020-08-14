from django.views import View
from django.shortcuts import render


# Create your views here.
class Index(View):
    @staticmethod
    def get(request):
        template_name = 'index.html'
        title = 'Aspiring Black Coders'
        message = 'Aspiring Black Coders'
        statement = 'A community for people of color aspiring to begin and grow careers in tech together.'
        extra_context = {'message': message, 'statement': statement,
                         'title': title}
        return render(request, template_name, extra_context)
