from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")


def categories(request):
    return HttpResponse("<h1>Категории</h1>")
