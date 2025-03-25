'''Определяет схемы URL для learning_logs.'''
from django.urls import path, re_path
from . import views
urlpatterns=[
    #домашняя страница
    re_path(r'^$',views.index,name='index'),
    #вывод всех тем
    re_path(r'^topics/$',views.topics,name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    re_path(r'^edit_entry/(?P<topic_id>\d+)/$',views.edit_entry,name='edit_entry'),
    ]
