"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tasks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.list_tasks, name='home'),
    url(r'^create/', views.create_tasks, name='create_task'),
    url(r'^update-task/', views.update_task, name='update_task'),
    url(r'^complete-task/', views.complete_task, name='complete_task'),
    url(r'^delete-task/', views.delete_task, name='delete_task'),
    url(r'^archive-task/', views.archive_task, name='archive_task'),
]
