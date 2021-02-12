from django.urls import path

from ss411.ssoffices.views import SsOfficeDetailView, SsOfficeListView

app_name = 'ssoffices'

urlpatterns = [
    path('', SsOfficeListView.as_view(), name='list'),
    path('<slug:slug>/', SsOfficeDetailView.as_view(), name='detail'),
]


