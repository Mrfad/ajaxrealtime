from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('ajax/getUsers', getUsers, name='getUsers'),
    path('detail/id', detail, name='detail'),
]