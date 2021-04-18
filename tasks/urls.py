from django.urls import path, include
from .views import TaskListView

app_name= "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
]
