from django.http import HttpResponse
from django.template import loader

def homePageView(request):
     context = {
        'text': 'Hello Test!',
     }
     template = loader.get_template('home/index.html')
     return HttpResponse(template.render(context, request))