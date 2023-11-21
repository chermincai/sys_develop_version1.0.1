# home/urls.py
from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('introduction/',views.index,name='introduction'),
    path('dataset/', views.dataset, name='dataset'),
    path('online-test/text_test', views.text_test, name='text_test'),
    path('online-test/img_test', views.img_test, name='img_test'),
    path('online-test/short_video_test', views.short_video_test, name='short_video_test'),
    path('online-test/long_video_test', views.long_video_test, name='long_video_test'),
]
