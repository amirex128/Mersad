from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from member_app.models import Member


def index_member(req):
    pass


def create_member(req):
    member = Member(first_name="amir", last_name="shirdel", nation_code=int("0923657073"), phone=int("09024809753"))

    print(member.save())
    return HttpResponse('ok');
