from django.views.generic import TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'
    title = 'Aspiring Black Coders'
    message = 'Aspiring Black Coders'
    statement = 'A community for people of color aspiring to begin and grow careers in tech together.'
    extra_context = {'message': message, 'statement': statement,
                     'title': title}
