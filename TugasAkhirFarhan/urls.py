from django.contrib import admin
from django.urls import path
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('informasi/', informasi, name='informasi'),
    path('monitor/', get_pipeline_data, name='get_pipeline_data'),
]
