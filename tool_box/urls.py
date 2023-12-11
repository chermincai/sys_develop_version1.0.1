# tool_box/urls.py
from django.urls import path
from . import views
app_name = 'tool_box'
urlpatterns = [
    path('tool_box/porn_detection', views.porn_detection, name='porn_detection'),
]
