from django.shortcuts import render #This allows you to render the template 


#Function that takes an http request and returns the html template associated with the request
def index(request):
    message = "Hello, you are now at the Aspiring Black Coders home page!"
    template_name = "index.html"
    context = {'message': message} #Can be displayed using double curly brace notation in your html template
    return render(request, template_name, context)


def mission(request):
    message = "This is ABC's mission statement."
    statement = "Insert mission statement below."
    template_name = "mission.html"
    context = {'message': message, 'statement': statement}
    return render(request, template_name, context)