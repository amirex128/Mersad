from django.shortcuts import render


def home_main(req):
    return render(req,'index.html')
