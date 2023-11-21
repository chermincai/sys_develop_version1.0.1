# home/views.py
import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    template_path = os.path.join(settings.BASE_DIR,'templates','index.html')
    return render(request, template_path)

def dataset(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'dataset.html')
    return render(request, template_path)


def text_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'text-test.html')
    return render(request, template_path)


def img_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'img-test.html')
    return render(request, template_path)
def short_video_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'short_video-test.html')
    return render(request, template_path)
def long_video_test(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'long_video-test.html')
    return render(request, template_path)