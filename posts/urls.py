
from django.urls import path, include, re_path
from posts.views import (post_delete,
                         post_update,
                         post_create,
                         post_detail,
                         post_list)


app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/edit/', post_update, name='post_update'),
    path('<slug:slug>/delete/', post_delete, name='post_delete'),
]