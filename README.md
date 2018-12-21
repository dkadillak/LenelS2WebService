# LenelS2WebService


## Functionality
* Returning a list of all created people 
```
GET localhost:5000/person
```
* Creating a person
```
POST localhost:5000/person
```
* Removing a person
```
DELETE localhost:5000/person/{id}
```
* Returning a list of people whose first/last name equals {filter}
```
GET localhost:5000/person?filter={filter}
```
* Returning person matching this id
```
GET localhost:5000/person/{id}
```

* Modifying a person specified by a given id
```
PUT localhost:5000/person/{id}
```

### Person format
{
  "id": X,
  "first_name": "fname",
  "last_name": "lname"
}

### Response format when expecting data
When calling ```GET /person``` or ```GET /person?filter={filter}```
```
{
    
    "people": "[Person1,Person2,Person3]"

}

```
When calling ```GET /person/{id}```
```
{
    
    "person": "{"id": X, "first_name": "fname", "last_name": "lname"}"

}
```

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

## Design Decisions
* a person's id must be unique
* a person's id must be a positive integer >= 1
* a person's fields will be maintained if any fields are left blank in a PUT request's body
```
request: PUT /person/1
body: 
{
    "id": "",
    "first_name": "Steve",
    "last_name": "Steverson"
    
}
```
assuming a person exists with id equal to 1, the "id" field of that person will remain 1 after the PUT request
* a person's first and last name will fit a given {filter} if the filter equals the first/last name or if the filter is contained in a substring of the first/last name
```
GET /person?filter=d 
```
will return all people whose first/last name contain the letter 'd' in it



