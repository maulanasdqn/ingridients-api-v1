from django.shortcuts import render
from django.http import JsonResponse

def Ingridients(request, *args, **kwargs):
    return JsonResponse({
        "message": "anjay mabar"
        })
