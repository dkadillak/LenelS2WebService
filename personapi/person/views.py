
from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


# handles a lot of the basic rest requests
class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


'''
Custom functions in progress: 

def get_hi(request):
    return HttpResponse("Hello World", content_type="text/plain")


def query_by_id(pid, request):
    if request.method == 'GET':
        print(pid)

        try:
            person = Person.objects.get(pid=pid)
            response = json.dumps([{'id': person.pid, 'first_name': person.first_name, 'last_name': person.last_name}])
        except:
            response = json.dumps([{'Error': 'Person could not be found'}])

    return HttpResponse("hey ya fuck", content_type="text/plain")


def create_person(request):
    if request.method == 'POST':
        
        payload = json.loads(request.body)
        pid = payload["id"]
        first_name = payload["first_name"]
        last_name = payload["last_name"]
        person = Person(id=pid, first_name=first_name, last_name=last_name)
        try:
            person.save()
            response = json.dumps([{'Success': 'Person was created successfully'}])
        except:
            response = json.dumps([{'Error': 'Person could not be created'}])
        
        return HttpResponse("your on poop", content_type='text/plain')

    else:
        print(request.method)
        return HttpResponse("your on poopoo", content_type='text/plain')

'''




