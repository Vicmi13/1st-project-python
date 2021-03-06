from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world ")
    else:
        return HttpResponse("Hello world " + name)

def home(request):
    latest_movies = Movie.objects.all()
    context = {'movies':latest_movies}
    return render(request, "home.html", context)


