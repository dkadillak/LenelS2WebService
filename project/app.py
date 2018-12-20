from flask import Flask, request, Response
from project.Validator import Validator
from project.Person import Person
import json

# telling flask what package my app is in
app = Flask('project')

# instance variable which will store person objects
personStorage = Validator()


@app.route('/person/', methods=['GET'])
def get_all_people():
    person_filter = request.args.get('filter')
    if person_filter is None:
        p_list = json.dumps({"people": str(personStorage.person_list)})
        resp = Response(p_list, status=200, mimetype='application/json')
        return resp
    else:
        p_list = json.dumps({"people": str(personStorage.create_list_by_filter(person_filter))})
        resp = Response(p_list, status=200, mimetype='application/json')
        return resp


@app.route('/person/', methods=['POST'])
def create_person():
    data = request.get_json()
    # send this data to validity checker
    p = Person(data['id'], data['first_name'], data['last_name'])
    if personStorage.add_person(p):

        return Response("Successfully added person!", status=201)
    else:
        return Response("ERROR: person already exists", status=400)


@app.route('/person/<person_id>', methods=['DELETE'])
def delete_person(person_id):
    index = personStorage.does_id_exist(person_id)
    if index != -1:
        personStorage.person_list.remove(personStorage.person_list[index])
        return Response("Deleted person with id: "+person_id, status=200)
    else:
        return Response("ERROR: person with id "+person_id+" does not exist", status=400)


@app.route('/person/<person_id>', methods=['GET'])
def get_person_by_id(person_id):
    index = personStorage.does_id_exist(person_id)
    if index != -1:
        return Response(json.dumps({"person": str(personStorage.person_list[index])}), status=200)
    else:
        return Response("ERROR: person with id " + person_id + " does not exist", status=400)


@app.route('/person/<person_id>', methods=['PUT'])
def edit_person_by_id(person_id):
    data = request.get_json()
    new_id = data['id']
    new_first = data['first_name']
    new_last = data['last_name']

    if personStorage.modify_person(person_id, new_id, new_first, new_last):
        return Response("Person with id "+person_id+" was successfully modified", status=200)
    else:
        return Response("ERROR: person with id " + person_id + " does not exist", status=400)





