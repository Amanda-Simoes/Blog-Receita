from django.urls import path
from .views import home, add

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home.as_view(), name='home'),
    path('home/add/', add.as_view(), name='add')
]