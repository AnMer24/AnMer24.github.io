'''Определяет схемы URL для users.'''
from django.urls import path, re_path
from . import views
urlpatterns=[
    re_path(r'^login/$',views.login_view,name='login'),
    re_path(r'^logout/$',views.logout_view, name='logout'),
    re_path(r'register/$',views.register_view,name='register'),
    ]

