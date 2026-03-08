from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'vitalsync.html')

urlpatterns = [
    path('', home),
    path('api/', include('cedulas_proxy.urls')),
]