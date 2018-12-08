# LenelS2WebService


## Functionality
* Returning a list of all created people 
```
GET /api/people
```
* Returning a list of people matching given first/last name => filter
```
GET /api/people?filter={filter}
```
* Returning person matching this id
```
GET / api/people/{id}
```
* Creating a person
```
POST /api/people
```
* Creating a person (idempotent)
```
PUT /api/people/{id}
```
* Removing a person
```
DELETE /api/people/{id}
```

### Person format
{
  "id": X,
  "first_name": "fname",
  "last_name": "lname"
}

## Running
Once Python3 is installed and repo is cloned, navigate to the root directory of the project:
```
~/LenelS2WebService$ pip3 install -r requirements.txt
```

Once dependencies have been installed, navigate to /personapi 
```
~/LenelS2WebService/personapi$ python3 manage.py runserver
```
Now send API requests to http://localhost:8000/

## Assumptions
* A person's id field must be unique

## Built With
* Python 3.7.1 
* Django 2.1.4 
