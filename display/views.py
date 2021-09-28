from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import User, School
from django.core import serializers
import json

def index(request):
    return render(request, 'index.html')

def getUsers(request):
    queryset = User.objects.all()[:20]
    return JsonResponse({'users':list(queryset.values("userId", "name", "phone","email", "school_name__sch_name"))})


def detail(request, id):
    qs = User.objects.get(id=id)
    context = {'qs':qs}
    return render(request, 'detail.html', context)