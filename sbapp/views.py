from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
# Create your views here.

def home(request : HttpRequest):
    return JsonResponse({'message' : 'Тут будет сайт :)'})