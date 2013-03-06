from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from log.models import log_page
# Create your views here.

def home_page(request):
    template = loader.get_template('index.html')
    latest_log_list = log_page.objects.all()[:5]
    context = RequestContext(request, {'log_page': latest_log_list})
    return HttpResponse(template.render(context))

    
