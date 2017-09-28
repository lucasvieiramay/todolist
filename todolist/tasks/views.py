from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Tasks


@csrf_exempt
def list_tasks(request):
    all_tasks = Tasks.objects.filter(
        completed=False, archived=False).order_by('label')
    data_to_render = {
        'tasks': all_tasks,
    }

    return render(
        request, 'tasks.html', data_to_render)


@csrf_exempt
def create_tasks(request):
    if request.POST:
        title = request.POST.get('title')
        label = request.POST.get('label')
        Tasks.objects.create(
            title=title, label=label,
        )
        return redirect('/')

    return render(
        request, 'create-task.html')


@csrf_exempt
def update_task(request):
    if request.POST:
        task_id = request.POST.get('task_id')
        title = request.POST.get('title')
        Tasks.objects.filter(pk=task_id).update(
            title=title
        )
        return redirect('/')


@csrf_exempt
def complete_task(request):
    if request.POST:
        task_id = request.POST.get('task_id')
        Tasks.objects.filter(pk=task_id).update(
            completed=True
        )
        return redirect('/')
