from django.shortcuts import render, redirect, HttpResponse
import requests



def home(request):
    template = 'home.html'
    return render(request, template)

def informasi(request):
    template = 'informasi.html'
    return render(request, template)

def get_pipeline_data(request):
    access_token = 'glpat-QhAKD253UX8cc9CLJKMs'  
    # api_url = 'https://gitlab.com/api/v4/projects/56091294/pipelines/1223616642/'
    api_url = 'https://gitlab.com/api/v4/projects/56091294/jobs'
    headers = {'PRIVATE-TOKEN': access_token}
    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        context = {'pipeline_data': data}
        template = 'pipeline.html'
        return render(request, template, context)
    except Exception as e:
        error_message = str(e)
        context = {'error_message': error_message}
        template = 'pipeline.html'
        return render(request, template, context)