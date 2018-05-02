from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.create_task, name='add'),
    path('complete/<task_id>', views.complete_task, name='complete'),
    path('delete', views.delete_task, name='delete'),
    path('delete_all', views.delete_all, name='delete_all')
]
