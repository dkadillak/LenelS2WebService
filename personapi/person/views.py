
from django.shortcuts import render
from django.http import HttpResponse


def get_hi(request):
    return HttpResponse("Hello World", content_type="text/plain")

