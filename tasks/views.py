from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    TemplateView
)

from django.urls import reverse_lazy

from tasks.models import Task
from tasks.forms import TaskForm


class TaskListView(LoginRequiredMixin ,ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(created_by=user)
        return queryset

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task-list')


    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task-list')


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/dashboard.html'