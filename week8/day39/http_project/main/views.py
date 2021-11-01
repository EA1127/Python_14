from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    print(request)
    return render(request, 'index.html')

def detail(request):
    return render(request, 'detail.html')
