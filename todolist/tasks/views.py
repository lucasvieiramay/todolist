from django.shortcuts import render
from django.shortcuts import redirect

from tasks.models import Tasks


def list_tasks(request):

    all_tasks = Tasks.objects.filter(
        completed=False, archived=False).order_by('label')
    data_to_render = {
        'tasks': all_tasks,
    }

    return render(
        request, 'tasks.html', data_to_render)


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
