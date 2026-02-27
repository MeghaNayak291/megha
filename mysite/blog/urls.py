# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:33:45 2026

@author: DELL
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('api/posts/', views.post_list_api),
    path('api/posts/create/', views.post_create_api),
    path('api/posts/<int:pk>/update/',views.post_update_api),
    path('api/posts/<int:pk>/delete/',views.post_delete_api),

]