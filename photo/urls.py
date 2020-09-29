from django.urls import path
from .views import *
from django.views.generic.detail import  DetailView
from .models import Photo
app_name='photo'
# 2차 URL 파일


urlpatterns=[
    #함수형뷰여서 as_view안붙음
    #127.0.0.1:8000/abcd/도 빈칸으로 들어감
    path('',photo_list ,name='photo_list'),
    path('detail/<int:pk>/',DetailView.as_view(model=Photo, template_name='photo/detail.html'),name='photo_detail'),
    #별로 들어갈내용없으면 views.py에 있어야 하는걸 urls에 옮겨놈
    path('upload/',PhotoUploadView.as_view(),name='photo_upload'),
    path('delete/<int:pk>/',PhotoDeleteView.as_view(),name='photo_delete'),
    path('update/<int:pk>',PhotoUpdateView.as_view(),name='photo_update'),
]