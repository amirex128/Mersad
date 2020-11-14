from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index_report(req):
    return HttpResponse('index_report')


def create_report(req):
    return HttpResponse('create_report')
