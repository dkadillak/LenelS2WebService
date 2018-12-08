from django.shortcuts import render

from django.http import HttpResponse
'''
from rest_framework.views import APIView
from rest_framework.response import Response
import json
'''


class person:

    json = {}

    def __init__(self, pid, first, last):

        #do some unique pid verification here
        self.json["id"] = pid
        self.json["first_name"] = first
        self.last_name = last


def get_hi(request):
    print("get_hi was called")
    return HttpResponse("Hello World", content_type="text/plain")
