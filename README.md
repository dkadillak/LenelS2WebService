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
```
{
  "id": X,
  "first_name": "fname",
  "last_name": "lname"
}
```

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
* a person's first_name and last_name fields will be maintained if they are left blank in a PUT request's body

###Person we're modifying:
```
{
  "id": 1,
  "first_name": "Steve",
  "last_name": "Steverson"
}
```
###request: PUT /person/1
```
body: 
{
    "id": 14,
    "first_name": "",
    "last_name": "Steve-man"
    
}
```
###Result:
```
{
  "id": 14,
  "first_name": "Steve",
  "last_name": "Steve-man"
}
```

* ``` GET /person?filter``` will return all people whose first/last name contain the letter 'd' in it
```
GET /person?filter=d 
```





