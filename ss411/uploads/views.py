from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, FormView
from django.views.generic.list import ListView
from django.utils import timezone
from ss411.uploads.models import UploadFile
from ss411.uploads.forms import UploadFileForm

# from ss411.uploads.templates.uploads import UploadTemplate

class UploadCreateView(CreateView):
    model=UploadFile
    form_class = UploadFileForm
    template_name = 'upload.html'

class UploadDetailView(DetailView):
    model=UploadFile
    form_class = UploadFileForm
    template_name = 'upload.html'

class UploadFormView(FormView):
    model=UploadFile
    template_name = 'upload.html'
    form_class = UploadFileForm
    success_url = ''





