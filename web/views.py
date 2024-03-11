from django.shortcuts import render, redirect, HttpResponse


def home(request):
    template = 'home.html'
    return render(request, template)
