from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# 📝 List all tasks (only for logged-in user)
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")  # Show only user's tasks
    return render(request, "tasks_management/task_list.html", {"tasks": tasks})

# ➕ Create a new task
@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign task to the logged-in user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks_management/task_form.html", {"form": form, "action": "Create Task"})

# ✏ Update an existing task
@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Only allow updating own tasks
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks_management/task_form.html", {"form": form, "action": "Update Task"})

# 🗑 Delete a task
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "tasks_management/task_confirm_delete.html", {"task": task})
