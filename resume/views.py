from django.conf import settings
from django.shortcuts import render
from .models import ResumeFile
import os
from django.http import HttpResponse, Http404
# Create your views here.

def home(request):
    file = ResumeFile.objects.all()

    return render(request, 'index.html', {'file':file}) 

def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/resume")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response 
    raise Http404     