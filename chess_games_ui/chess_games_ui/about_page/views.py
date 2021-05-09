from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    # template = loader.get_template('about_page/tmp.html')
    # context = {}
    # return HttpResponse(template.render(context, request))
    return render(request, 'about_page/about_page.html')

