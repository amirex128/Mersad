from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_rule(req):
    return HttpResponse('index_rule')


def create_rule(req):
    return HttpResponse('create_rule')
