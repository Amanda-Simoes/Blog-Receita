from django.urls import path
from .views import home, add

urlpatterns = [
    path('home/', home.as_view(), name='home'),
    path('home/add/', add.as_view(), name='add')
]
