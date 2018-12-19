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
    person_filter = request.args.get('filter')
    if person_filter is None:
        return str(personStorage.person_list)
    else:
        return str(personStorage.create_list_by_filter(person_filter))


@app.route('/person/', methods=['POST'])
def create_person():
    data = request.get_json()
    p = Person(data['id'], data['first_name'], data['last_name'])
    if personStorage.add_person(p):
        return "Successfully added person!"
    else:
        return "Error: didn't add person"


@app.route('/person/<person_id>', methods=['DELETE'])
def delete_person(person_id):
    index = personStorage.does_id_exist(person_id)
    if index != -1:
        personStorage.person_list.remove(personStorage.person_list[index])
        return "Deleted person with id: "+person_id

    else:
        return "Error: person with id "+person_id+" does not exist"


@app.route('/person/<person_id>', methods=['GET'])
def get_person_by_id(person_id):
    index = personStorage.does_id_exist(person_id)
    if index != -1:
        return str(personStorage.person_list[index])
    else:
        return "Error: person with id " + person_id + " does not exist"








