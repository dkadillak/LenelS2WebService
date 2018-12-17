from flask import Flask, request, app
from project.Validator import Validator
from project.Person import Person
import json

# telling flask what package my app is in
app = Flask('project')

# instance variable which will store person objects
personStorage = Validator()
# personStorage.add_person(Person('1', 'devin', 'kadillak'))
# personStorage.add_person(Person('2', 'steve', 'mcballsack'))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/person/', methods=['GET'])
def get_all_people():

    return str(personStorage.person_list)


@app.route('/person/', methods=['POST'])
def create_person():
    data = request.get_json()
    p = Person(data['id'], data['first_name'], data['last_name'])
    if personStorage.add_person(p):
        return "Successfully added person!"
    else:
        return "Error: didn't add person"


def validate_payload(req):
    return 0






