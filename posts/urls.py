
from django.urls import path, include
from posts.views import (post_delete,
                         post_update,
                         post_create,
                         post_detail,
                         post_list)


app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('<int:id>/edit/', post_update, name='post_update'),
    path('<int:id>/delete/', post_delete, name='post_delete'),
]
