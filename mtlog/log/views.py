from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from log.models import log_page_model
from log.forms import log_form
# Create your views here.

def home_page(request):
#    template = loader.get_template('index.html')
    log_pages = log_page_model.objects.all()[:5]
#    context = RequestContext(request, {'log_pages': log_pages})
#    return HttpResponse(template.render(context))
    return render_to_response('index.html', RequestContext(request, {'log_pages': log_pages}))


def log_form_page(request):
#    template = loader.get_template('base_form.html')
    if request.method == 'POST':
        forms = log_form(request.POST)
        if forms.is_valid():
            db = log_page_model(log_title=forms.cleaned_data['log_title'], author=forms.cleaned_data['author'], contents=forms.cleaned_data['contents'])
            db.save()
            return HttpResponseRedirect('/')
    else:
        forms = log_form()
#    context = RequestContext(request, {'forms', forms})    
#    return HttpResponse(template.render(context))
    return render_to_response('base_form.html', RequestContext(request, {'forms':forms}))

def about_page(request):
    return render_to_response('base_about.html', RequestContext(request,{}))





