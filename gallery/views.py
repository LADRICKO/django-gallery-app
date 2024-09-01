# gallery/views.py

from django.shortcuts import render
from .models import Image

def gallery_view(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})

# Create your views here.
