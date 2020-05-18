from django.urls import path
from .views import  home, create,task_delete, completed_task

urlpatterns = [
        path("home/",home, name="home"),
        path("create/",create, name="create"),
        path("completed_task/",completed_task, name="completed-tasks"),
        path('<int:pk>/delete/', task_delete.as_view(), name='task_delete'),

 ]
