from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_safe, require_http_methods
from rest_framework.parsers import JSONParser

from accused_app.forms import AccusedForm
from accused_app.models import Accused
from accused_app.serializers import AccusedSerializer


@require_GET
def index_accused(req):
    accuseds = Accused.objects.all()
    accused_serializer = AccusedSerializer(accuseds, many=True)
    return JsonResponse(accused_serializer.data, safe=False)


@require_GET
def show_create_accused(req):
    context = {
        'form': AccusedForm()
    }
    return render(req, 'accused_app/create.html', context)


@csrf_exempt
@require_POST
def create_accused(req):
    parse = JSONParser().parse(req)
    accused_serializer = AccusedSerializer(data=parse)
    if accused_serializer.is_valid():
        accused_serializer.save()
        return JsonResponse('ok', safe=False)
    else:
        return JsonResponse(accused_serializer.errors, safe=False)


@csrf_exempt
@require_http_methods(['post', 'put'])
def update_accused(req, accused_id):
    accused = get_object_or_404(Accused, id=accused_id)
    print(accused)
    return render(req, 'accused_app/update.html', {'accused': accused})
