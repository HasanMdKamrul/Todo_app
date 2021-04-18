from django.urls import path, include
from .views import TaskListView,TaskCreateView

app_name= "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
]
