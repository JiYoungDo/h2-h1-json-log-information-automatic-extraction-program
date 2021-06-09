from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# Create your views here.

class Home(TemplateView):
        template_name = 'base.html'

def upload(request):
        if request.method == 'POST':
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(uploaded_file.name, uploaded_file)
                
                print(uploaded_file.name)
                print(uploaded_file.size )
        return render(request, 'upload.html') 