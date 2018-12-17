# LenelS2WebService


## Implemented Functionality
* Returning a list of all created people 
```
GET localhost:8000/people
```
* Creating a person
```
POST localhost:8000/people
```

## NonImplemented Functionality
* Modifying a person specified by a given id
```
PUT localhost:8000/people/{id}
```
* Removing a person
```
DELETE localhost:8000/people/{id}
```
* Returning a list of people matching given first/last name => filter
```
GET /api/people?filter={filter}
```
* Returning person matching this id
```
GET / api/people/{id}
```
### Person format
{
  "id": X,
  "first_name": "fname",
  "last_name": "lname"
}

## Running
Once Python3 is installed and repo is cloned, navigate to the root directory of the project and execute:
```
~/LenelS2WebService$ pip3 install -r requirements.txt
```


Once dependencies have been installed, navigate to /project, and set FLASK_APP
```
~/LenelS2WebService/project$ export FLASK_APP=app.py
```
Run the server with 
```
~/LenelS2WebService/project$ flask run
```
Now send API requests to http://127.0.0.1:5000/person/

## Built With
* Python 3.7.1 
* Flask 1.0.2

