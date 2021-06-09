from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
        template_name = 'base.html'

def upload(request):
    return render(request, 'upload.html')