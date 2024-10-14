from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('create_task/', views.create_task, name='create_task'),
    path('notifications/', views.notifications, name='notifications'),
]
