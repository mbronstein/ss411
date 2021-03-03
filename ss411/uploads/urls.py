from django.urls import path
from ss411.uploads.views import UploadCreateView, UploadDetailView, UploadFormView
app_name = 'uploads'

urlpatterns = [
    path('', UploadFormView.as_view(), name='upload'),
    path('add/', UploadCreateView.as_view(), name='upload'),
    path('<int:pk>', UploadDetailView.as_view(), name='detail'),
]
