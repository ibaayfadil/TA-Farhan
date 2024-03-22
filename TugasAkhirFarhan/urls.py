from django.contrib import admin
from django.urls import path
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('informasi/', informasi, name='informasi'),
    path('pipeline/', get_pipeline_data, name='pipeline'),
]
