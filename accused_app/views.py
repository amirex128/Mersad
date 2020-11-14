from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from accused_app.models import Accused


# Create your views here.


@csrf_exempt
def index_accused(req):
    return JsonResponse({
        'page': 'index accused'
    })


def create_accused(req):
    return render(req, 'accused_app/create.html')


def update_accused(req, accused_id):
    accused = get_object_or_404(Accused, id=accused_id)
    print(accused)
    return render(req, 'accused_app/update.html', {'accused': accused})
