from django.urls import path
from tasks import views


urlpatterns = [
    path('list/', views.TaskListView.as_view(), name="task-list"),
    path('create/', views.TaskCreateView.as_view(), name="task-create"),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name="task-update"),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name="task-delete"),
]