from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import models
import re
import json

def home(request):
    return HttpResponse("Inicio")

@csrf_exempt
def send_messages(request):
    try:
        models.send_whatsapp_request(
            get_key_request(request,"message"),
            get_number_list(get_key_request(request,"phoneList")),
            get_key_request(request,"image"),
            get_key_request(request,"imageName"),
            request.META.get('REMOTE_ADDR').replace('.','')
        )
        return JsonResponse({"message":"Mensajes enviados"})
    except Exception as e:
        print(e)
        return JsonResponse({"message":"No se han podido enviar los mensajes"})

def get_key_request(request, key):
    return request.POST.get(key) if request.POST != {} else json.loads(request.body)[key]

def get_number_list(numbersString):
    return [number.replace("\n","").replace("\r","").replace(" ","") for number in re.split(r"[,;]",numbersString) if number.strip()]
