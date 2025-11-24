from django.urls import path
from main.views import TaskList
from  . import views

urlpatterns = [
    path("testest", TaskList.as_view(), name='task_list'),
    path('', views.task_list, name= 'task_list_função'),
    path('tarefas_concluidas', views.task_concluido, name='task_concluida') 
]