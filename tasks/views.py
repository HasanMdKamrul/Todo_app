from django.shortcuts import render
from django.views import generic
from .models import Task
 


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return super().get_queryset()
    


