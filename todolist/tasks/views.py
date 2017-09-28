from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Tasks


@csrf_exempt
def list_tasks(request):
    show_archived = request.GET.get('showArchived', False)

    if show_archived:
        all_tasks = Tasks.objects.filter(
            completed=False).order_by('label')
    else:
        all_tasks = Tasks.objects.filter(
            completed=False, archived=show_archived).order_by('label')

    data_to_render = {
        'tasks': all_tasks,
    }

    return render(
        request, 'tasks.html', data_to_render)


@csrf_exempt
def create_tasks(request):
    if not request.POST:
        return HttpResponse(status=403)

    title = request.POST.get('title')
    label = request.POST.get('label')
    Tasks.objects.create(
        title=title, label=label,
    )
    return redirect('home')


@csrf_exempt
def update_task(request):
    if not request.POST:
        return HttpResponse(status=403)

    task_id = request.POST.get('task_id')
    title = request.POST.get('title')
    Tasks.objects.filter(pk=task_id).update(title=title)
    return redirect('home')


@csrf_exempt
def complete_task(request):
    if not request.POST:
        return HttpResponse(status=403)

    task_id = request.POST.get('task_id')
    Tasks.objects.filter(pk=task_id).update(
        completed=True
    )
    return HttpResponse()


@csrf_exempt
def delete_task(request):
    if not request.POST:
        return HttpResponse(status=403)

    task_id = request.POST.get('task_id')
    Tasks.objects.filter(pk=task_id).delete()
    return HttpResponse()


@csrf_exempt
def archive_task(request):
    if not request.POST:
        return HttpResponse(status=403)

    task_id = request.POST.get('task_id')
    Tasks.objects.filter(pk=task_id).update(
        archived=True
    )
    return HttpResponse()
