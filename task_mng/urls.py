from django.urls import path
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path("", task_list, name="task_list"),  # View all tasks
    path("create/", task_create, name="task_create"),  # Add a new task
    path("update/<int:task_id>/", task_update, name="task_update"),  # Edit a task
    path("delete/<int:task_id>/", task_delete, name="task_delete"),  # Delete a task
]
