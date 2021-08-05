from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView


def index(request):
    return render(request, 'home_page.html')