from django.shortcuts import render, redirect, HttpResponse
import requests



def home(request):
    template = 'home.html'
    return render(request, template)

def informasi(request):
    template = 'informasi.html'
    return render(request, template)

def get_pipeline_data(request):
    api_url = 'https://gitlab.com/api/v4/projects/54304174/pipelines'
    try:
        response = requests.get(api_url)
        data = response.json()
        context = {'pipeline_data': data}
        template = 'get_pipeline_data.html'
        return render(request, template, context)
    except Exception as e:
        error_message = str(e)
        context = {'error_message': error_message}
        template = 'get_pipeline_data.html'
        return render(request, template, context)
