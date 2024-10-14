from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ComplianceTask, Notification
from .forms import TaskForm


#@login_required
def dashboard(request):
    tasks = ComplianceTask.objects.filter(assigned_to=request.user)
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'compliance/dashboard.html', {'tasks': tasks, 'notifications': notifications})

#@login_required
def task_list(request):
    tasks = ComplianceTask.objects.all() if request.user.is_staff else ComplianceTask.objects.filter(assigned_to=request.user)
    return render(request, 'compliance/task_list.html', {'tasks': tasks})

#@login_required
def create_task(request):
    if not request.user.is_staff:
        messages.error(request, 'Permission Denied')
        return redirect('dashboard')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'compliance/create_task.html', {'form': form})

# @login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'compliance/notifications.html', {'notifications': notifications})
