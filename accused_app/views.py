from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone

from accused_app.models import Accused


def index_accused(req):
    return HttpResponse('index_accused')


def create_accused(req):
    return HttpResponse('create_accused')


def update_accused(req, accused_id):
    accused = get_object_or_404(Accused, id=accused_id)
    print(accused)
    return render(req, 'accused_app/update.html', {'accused': accused})
