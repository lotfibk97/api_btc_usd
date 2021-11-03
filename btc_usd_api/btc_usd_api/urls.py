from django.contrib import admin
from django.urls import path
from api.views import GetRate, generate_api_key

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/quotes/<str:apikey>', GetRate.as_view(), name='getrate'),
    path('generate_key', generate_api_key, name='generate_api_key')
]
