from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns=[
    #登录视图
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    #注销
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册用户
    url(r'^register/$',views.register,name='register'),
]