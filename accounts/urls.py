from django.urls import path
from .views import *
#appname 여기서는 안씀
from django.contrib.auth import views as auth_view

#login하면 profile로 보내줌 → 근데 실제로 profilepage없다.

#1. profile page만들면됨
#2. profile 페이지가 아닌 페이지로 보내기 (장고 설정변경, 웹서버에서 redirect 하는방법이있음 )
urlpatterns=[
    path('login/',auth_view.LoginView.as_view(),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),#관리자페이지 로그아웃이되버
    path('register/',register,name='register'),
]