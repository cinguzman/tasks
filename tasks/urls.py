from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_tasks, name='list_tasks'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]
