from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.utils import timezone
import json
# Create your views here.

def get_cost(request):
    services = request.POST['text']
    try:
        import simplejson as json
    except (ImportError,):
        import json
    services = json.loads(services)
    cost = 0
    for item in services:
        cost = cost + Service.objects.get(id=int(item)).cost
    response = {}
    response['cost'] = cost
    return HttpResponse(json.dumps(response))


def get_patient(request):
    response = {}
    patient = request.POST['text']
    # print(patient)
    patient = Patient.objects.get(id=patient)
    response['isStaff'] = patient.sign
    try:
        response['policy'] = patient.policy_number.id
        response['balance'] = patient.policy_number.balance
    except Exception:
        response['policy'] = 0
        response['balance'] = 0
    # cost = 0
    # for item in services:
    #     cost = cost + Service.objects.get(id=int(item)).cost

    # response['cost'] = cost
    return HttpResponse(json.dumps(response))

def get_exempt(request):
    response = {}
    exempt = request.POST['text']
    exempt = Exempt.objects.get(id=exempt)
    response['exempt'] = exempt.exempt
    return HttpResponse(json.dumps(response))


def change_balance(request):
    response = {}
    balance = request.POST['text']
    patient = request.POST['patient']
    print(patient)
    patient = Patient.objects.get(id=patient)
    # try:
    patient.policy_number.balance = balance
    patient.policy_number.save()
    # except Exception:
    #     pass
    response['response'] = 'request is succesfull!'
    return HttpResponse(json.dumps(response))



