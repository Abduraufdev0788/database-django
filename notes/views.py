from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Task

def home_page(request: HttpRequest) -> HttpResponse:
    if request.method=="GET":
        return render(request=request, template_name="home_page.html")
    elif request.method=="POST":
        form = request.POST

        new_task = Task(
            name = form.get('name'),
            description = form.get('description'),
            statuse = form.get('statuse')
        )
        new_task.save()

    tasks = Task.objects.all()
    return render(request, "home_page.html", {"tasks": tasks})
        
