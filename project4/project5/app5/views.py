from django.shortcuts import render
from django.views.generic.list import ListView
from.models import Task
from django.http import HttpResponse

# Create your views here.
def Tasklist(ListView):
    model = Task
    context_object_name = 'tasks'