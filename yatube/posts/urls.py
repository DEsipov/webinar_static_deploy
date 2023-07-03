from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    path('', views.index, name='index'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('create/', views.post_create, name='post_create'),
]
