from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import FileForm
from .models import File



class Home(TemplateView):
        template_name = 'base.html'

def upload(request):
        context = {}
        if request.method == 'POST':
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                
                name = fs.save(uploaded_file.name, uploaded_file)
                # url = fs.url(name)
                context['url'] = fs.url(name)
                
                print(uploaded_file.name)
                print(uploaded_file.size )
                #print(url)
        return render(request, 'upload.html', context) 

def file_list(request):
        files = File.objects.all()
        return render(request, 'file_list.html',{
                'files': files
        })

def upload_file(request):
        if request.method == 'POST':
                form = FileForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect('file_list')
        else:
                form = FileForm()
        return render(request, 'file_upload.html',{
                'form': form
        }) 