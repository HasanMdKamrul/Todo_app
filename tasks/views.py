from django.shortcuts import render,reverse
from django.views import generic
from .models import Task
from .forms import TaskModelForm
 


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return super().get_queryset()


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "tasks/task_update.html"
    form_class = TaskModelForm
    context_object_name = "task"


    def get_success_url(self):
        return reverse("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    context_object_name = "task"

    def get_success_url(self):
        return reverse("tasks:task-list")
    


